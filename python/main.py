import sys

import lexer
import parse
import syntax


# Simple function to read a file
def readfile(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()


def main():
    # Get the code
    code = readfile(sys.argv[1])
    # Convert into tokens
    tokens = lexer.tokenize(code)
    # Do magic to get an ast
    ast = parse.parse(tokens)
    # Check syntax
    res = syntax.validate(ast)
    # If invalid, throw an error
    if type(res) == str:
        raise res
    # If not, then do nothing
    elif res == True:
        pass

if __name__ == '__main__':
    main()