# MGprogramming

MGprogramming is a new programming language inspired by Python but designed for Mongolian speakers.

## Prerequisites

- Python 3.x
- ANTLR 4.9.2

## Getting Started

### Setup

1. Clone the repository:

    ```sh
    git clone <your-repo-url>
    cd MGprogramming
    ```

2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Download ANTLR tool and generate lexer and parser:

    ```sh
    curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar
    java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 src/MGprogramming.g4 -o src
    ```

### Running the Interpreter

1. Run your code:

    ```sh
    python src/main.py your_code.mgp
    ```

### Running the CLI

1. Use the CLI:

    ```sh
    python cli/mgp_cli.py your_code.mgp
    ```

### Running Tests

1. Run tests using unittest:

    ```sh
    python -m unittest discover tests
    ```

## Project Structure

- `src/`: Source files, including the main script, lexer, parser, and interpreter.
- `cli/`: Command-line interface scripts.
- `tests/`: Test files.
- `.gitignore`: Git ignore file.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.
- `LICENSE`: License file.

## License

[MIT License](LICENSE)
