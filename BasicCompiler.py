import BasicLexer
import BasicParser
import sys

sys.setrecursionlimit(10000)

if __name__=='__main__':
    with open('testing_conversion.b','r') as file:
        parser=BasicParser.parser
        text=file.read()
        ast=parser.parse(text,lexer=BasicLexer.lexer)
        print(ast)