# Generated from AutomatonGrammar.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AutomatonGrammarParser import AutomatonGrammarParser
else:
    from AutomatonGrammarParser import AutomatonGrammarParser

# This class defines a complete listener for a parse tree produced by AutomatonGrammarParser.
class AutomatonGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by AutomatonGrammarParser#s.
    def enterS(self, ctx:AutomatonGrammarParser.SContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#s.
    def exitS(self, ctx:AutomatonGrammarParser.SContext):
        pass


    # Enter a parse tree produced by AutomatonGrammarParser#alfabeto.
    def enterAlfabeto(self, ctx:AutomatonGrammarParser.AlfabetoContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#alfabeto.
    def exitAlfabeto(self, ctx:AutomatonGrammarParser.AlfabetoContext):
        pass


    # Enter a parse tree produced by AutomatonGrammarParser#alf.
    def enterAlf(self, ctx:AutomatonGrammarParser.AlfContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#alf.
    def exitAlf(self, ctx:AutomatonGrammarParser.AlfContext):
        pass


    # Enter a parse tree produced by AutomatonGrammarParser#estados.
    def enterEstados(self, ctx:AutomatonGrammarParser.EstadosContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#estados.
    def exitEstados(self, ctx:AutomatonGrammarParser.EstadosContext):
        pass


    # Enter a parse tree produced by AutomatonGrammarParser#estado.
    def enterEstado(self, ctx:AutomatonGrammarParser.EstadoContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#estado.
    def exitEstado(self, ctx:AutomatonGrammarParser.EstadoContext):
        pass


    # Enter a parse tree produced by AutomatonGrammarParser#transicoes.
    def enterTransicoes(self, ctx:AutomatonGrammarParser.TransicoesContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#transicoes.
    def exitTransicoes(self, ctx:AutomatonGrammarParser.TransicoesContext):
        pass


    # Enter a parse tree produced by AutomatonGrammarParser#trans.
    def enterTrans(self, ctx:AutomatonGrammarParser.TransContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#trans.
    def exitTrans(self, ctx:AutomatonGrammarParser.TransContext):
        pass


    # Enter a parse tree produced by AutomatonGrammarParser#inicio.
    def enterInicio(self, ctx:AutomatonGrammarParser.InicioContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#inicio.
    def exitInicio(self, ctx:AutomatonGrammarParser.InicioContext):
        pass


    # Enter a parse tree produced by AutomatonGrammarParser#final.
    def enterFinal(self, ctx:AutomatonGrammarParser.FinalContext):
        pass

    # Exit a parse tree produced by AutomatonGrammarParser#final.
    def exitFinal(self, ctx:AutomatonGrammarParser.FinalContext):
        pass


