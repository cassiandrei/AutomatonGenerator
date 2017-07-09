import sys

from antlr4 import *

from AutomatonGrammarLexer import AutomatonGrammarLexer
from AutomatonGrammarParser import AutomatonGrammarParser
from AutomatonGrammarListener import AutomatonGrammarListener


class KeyPrinter(AutomatonGrammarListener):
    def enterS(self, ctx: AutomatonGrammarParser.SContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#s.
    def exitS(self, ctx: AutomatonGrammarParser.SContext):
        pass

    # Enter a parse tree produced by AutomatonGrammarParser#alfabeto.
    def enterAlfabeto(self, ctx: AutomatonGrammarParser.AlfabetoContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#alfabeto.
    def exitAlfabeto(self, ctx: AutomatonGrammarParser.AlfabetoContext):
        pass

    # Enter a parse tree produced by AutomatonGrammarParser#alf.
    def enterAlf(self, ctx: AutomatonGrammarParser.AlfContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#alf.
    def exitAlf(self, ctx: AutomatonGrammarParser.AlfContext):
        pass

    # Enter a parse tree produced by AutomatonGrammarParser#estados.
    def enterEstados(self, ctx: AutomatonGrammarParser.EstadosContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#estados.
    def exitEstados(self, ctx: AutomatonGrammarParser.EstadosContext):
        pass

    # Enter a parse tree produced by AutomatonGrammarParser#estado.
    def enterEstado(self, ctx: AutomatonGrammarParser.EstadoContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#estado.
    def exitEstado(self, ctx: AutomatonGrammarParser.EstadoContext):
        pass

    # Enter a parse tree produced by AutomatonGrammarParser#transicoes.
    def enterTransicoes(self, ctx: AutomatonGrammarParser.TransicoesContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#transicoes.
    def exitTransicoes(self, ctx: AutomatonGrammarParser.TransicoesContext):
        pass

    # Enter a parse tree produced by AutomatonGrammarParser#trans.
    def enterTrans(self, ctx: AutomatonGrammarParser.TransContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#trans.
    def exitTrans(self, ctx: AutomatonGrammarParser.TransContext):
        pass

    # Enter a parse tree produced by AutomatonGrammarParser#inicio.
    def enterInicio(self, ctx: AutomatonGrammarParser.InicioContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#inicio.
    def exitInicio(self, ctx: AutomatonGrammarParser.InicioContext):
        pass

    # Enter a parse tree produced by AutomatonGrammarParser#final.
    def enterFinal(self, ctx: AutomatonGrammarParser.FinalContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#final.
    def exitFinal(self, ctx: AutomatonGrammarParser.FinalContext):
        pass

    def visitTerminal(self, node):
        pass

    def visitErrorNode(self, node):
        print("Erro na entrada!!!!")
        exit(1);



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
