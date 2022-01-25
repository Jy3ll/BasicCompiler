from BasicCompiler import Compiler
import os

if __name__ =='__main__':
    filename=input("Please enter the name of file you want to compile: ")
    if not os.path.isfile(filename):
        print("Such file doesn't exist")
    else:
        my_compiler= Compiler()
        my_compiler.compile(filename)