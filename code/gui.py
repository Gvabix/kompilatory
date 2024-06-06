import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage
from antlr4 import *
from MGprogrammingLexer import MGprogrammingLexer
from MGprogrammingParser import MGprogrammingParser
from interpreter import Interpreter
from MyErrorListener import MyErrorListener


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill="white", font=('Consolas', 14))
            i = self.textwidget.index("%s+1line" % i)


class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self.linenumbers = None

    def attach_line_numbers(self, line_numbers):
        self.linenumbers = line_numbers

    def update_line_numbers(self, *args):
        if self.linenumbers:
            self.linenumbers.redraw()


class InterpreterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MG Programming Language Interpreter")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2b2b2b')

        # Header frame with buttons
        self.header_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.header_frame.pack(fill="x")

        # Create Run button
        self.run_button = tk.Button(self.header_frame, text="Run", command=self.run_code, bg='#4CAF50', fg='white',
                                    font=('Helvetica', 12, 'bold'), borderwidth=0, highlightthickness=0)
        self.run_button.pack(side=tk.TOP, padx=5, pady=5)

        # Create Clear button
        self.clear_button = tk.Button(self.header_frame, text="Clear", command=self.clear_output, bg='#f44336',
                                      fg='white', font=('Helvetica', 12, 'bold'), borderwidth=0, highlightthickness=0)
        self.clear_button.pack(side=tk.TOP, padx=5, pady=5)

        # Main frame with code editor and output area
        self.main_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Load background image
        self.background_image = PhotoImage(file="we2.png")

        # Add background image to the main frame
        self.background_label = tk.Label(self.main_frame, image=self.background_image)
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Create a frame for the code input and line numbers
        self.code_frame = tk.Frame(self.main_frame, bg='#2b2b2b')
        self.code_frame.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

        # Create line numbers
        self.line_numbers = TextLineNumbers(self.code_frame, width=30, bg='#2b2b2b')
        self.line_numbers.pack(side="left", fill="y")

        # Create text area for code input
        self.code_area = CustomText(self.code_frame, wrap=tk.WORD, bg='#424242', fg='white',
                                    font=('Consolas', 12), insertbackground='white', borderwidth=2, relief="solid")
        self.code_area.pack(side="right", fill="both", expand=True)

        self.line_numbers.attach(self.code_area)
        self.code_area.attach_line_numbers(self.line_numbers)

        # Bind events to update line numbers
        self.code_area.bind("<KeyRelease>", self.code_area.update_line_numbers)
        self.code_area.bind("<MouseWheel>", self.code_area.update_line_numbers)
        self.code_area.bind("<Button-1>", self.code_area.update_line_numbers)
        self.code_area.bind("<Return>", self.code_area.update_line_numbers)
        self.code_area.bind("<BackSpace>", self.code_area.update_line_numbers)
        self.code_area.bind("<Configure>", self.code_area.update_line_numbers)

        # Create output area
        self.output_area = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, state=tk.DISABLED,
                                                     bg='#424242', fg='white', font=('Consolas', 12), insertbackground='white', borderwidth=2, relief="solid")
        self.output_area.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)

    def run_code(self):
        code = self.code_area.get("1.0", tk.END)
        input_stream = InputStream(code)
        lexer = MGprogrammingLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = MGprogrammingParser(token_stream)

        error_listener = MyErrorListener()
        parser.removeErrorListeners()  # Remove the default error listeners
        parser.addErrorListener(error_listener)  # Add your custom error listener

        tree = parser.program()

        interpreter = Interpreter()

        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        try:
            interpreter.visit(tree)
            output = sys.stdout.getvalue()
            errors = error_listener.getErrors()

            if errors:
                output += "\n" + "\n".join(errors)
        except Exception as e:
            output = f"Runtime error: {str(e)}"

        # Restore stdout
        sys.stdout = old_stdout

        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete("1.0", tk.END)
        self.output_area.insert(tk.END, output)
        self.output_area.config(state=tk.DISABLED)

    def clear_output(self):
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete("1.0", tk.END)
        self.output_area.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    gui = InterpreterGUI(root)
    root.mainloop()
