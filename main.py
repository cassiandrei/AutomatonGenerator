import sys

from antlr4 import *

from AutomatonGrammarLexer import AutomatonGrammarLexer
from AutomatonGrammarParser import AutomatonGrammarParser
from AutomatonGrammarListener import AutomatonGrammarListener


class KeyPrinter(AutomatonGrammarListener):
    def exitS(self, ctx):
        print("Oh, o vinni apareceu")


def main(argv):
    input = FileStream(argv[1])
    lexer = AutomatonGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AutomatonGrammarParser(stream)
    tree = parser.s()

    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)
