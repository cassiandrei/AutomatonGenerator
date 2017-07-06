import sys
from antlr4 import *
from MyGrammarLexer import AutomatonGrammarLexer
from MyGrammarParser import AutomatonGrammarParser
 
def main(argv):
    input = FileStream(argv[1])
    lexer = AutomatonGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AutomatonGrammarParser(stream)
    tree = parser.startRule()
    
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
 
if __name__ == '__main__':
    main(sys.argv)
