import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage
from antlr4 import *
from MGprogrammingLexer import MGprogrammingLexer
from MGprogrammingParser import MGprogrammingParser
from Interpreter import Interpreter
from MyErrorListener import MyErrorListener


class InterpreterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MG Programming Language Interpreter")
        self.root.geometry("2560x1280")
        self.root.configure(bg='#f0f0f0')

        # Load background image
        self.background_image = PhotoImage(file="background.png")

        # Number of rows and columns for the grid
        self.rows = 4
        self.columns = 5

        # Determine the size of each cell in the grid
        cell_width = self.background_image.width()
        cell_height = self.background_image.height()

        # Create a frame to hold the grid
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(fill="both", expand=True)

        # Add frames for each cell in the grid
        for row in range(self.rows):
            for column in range(self.columns):
                frame = tk.Frame(self.grid_frame, width=cell_width, height=cell_height)
                frame.grid(row=row, column=column, padx=0, pady=0, sticky="nsew")
                frame.grid_propagate(False)  # Prevent frame from resizing

                # Add a label with the background image to each frame
                label = tk.Label(frame, image=self.background_image)
                label.pack(fill="both", expand=True)

        # Add the main application widgets
        self.add_main_widgets()

    def add_main_widgets(self):
        # Create title label
        self.title_label = tk.Label(self.root, text="MG Programming Language Interpreter", bg='#ffffff', fg='black',
                                    font=('Helvetica', 20, 'bold'))
        self.title_label.place(relx=0.35, rely=0.1, anchor="center")

        # Create label for code area
        self.code_label = tk.Label(self.root, text="Enter your code below:", bg='#ffffff', fg='black',
                                   font=('Helvetica', 14))
        self.code_label.place(relx=0.35, rely=0.2, anchor="center")

        # Create text area for code input
        self.code_area = tk.scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=15, bg='#ffffff', fg='black',
                                                      font=('Consolas', 12), insertbackground='black', borderwidth=2, relief="solid")
        self.code_area.place(relx=0.35, rely=0.4, anchor="center")

        # Create a frame for buttons
        self.button_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.button_frame.place(relx=0.35, rely=0.5, anchor="center")

        # Create Run button
        self.run_button = tk.Button(self.button_frame, text="Run", command=self.run_code, bg='#4CAF50', fg='black',
                                    font=('Helvetica', 12, 'bold'), borderwidth=0, highlightthickness=0)
        self.run_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create Clear button
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_output, bg='#f44336',
                                      fg='black', font=('Helvetica', 12, 'bold'), borderwidth=0, highlightthickness=0)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create label for the output area
        self.output_label = tk.Label(self.root, text="Output:", bg='#ffffff', fg='black', font=('Helvetica', 14))
        self.output_label.place(relx=0.35, rely=0.6, anchor="center")

        # Create text area for output
        self.output_area = tk.scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=10, state=tk.DISABLED,
                                                        bg='#ffffff', fg='black', font=('Consolas', 12), insertbackground='black', borderwidth=2, relief="solid")
        self.output_area.place(relx=0.35, rely=0.75, anchor="center")

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
