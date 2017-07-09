import sys

from antlr4 import *

from antlr.AutomatonGrammarLexer import AutomatonGrammarLexer
from antlr.AutomatonGrammarParser import AutomatonGrammarParser
from antlr.AutomatonGrammarListener import AutomatonGrammarListener


class Automato(AutomatonGrammarListener):
    alfabeto = []
    estados = []
    transicoes = []
    inicio = ""
    final = []

    def enterAlf(self, ctx:AutomatonGrammarParser.AlfContext):
        self.alfabeto.append(ctx.letra().getText())
        pass

    def enterEstados(self, ctx:AutomatonGrammarParser.EstadosContext):
        self.estados = ctx.estado().getText().split(",")
        pass

    def enterTrans(self, ctx:AutomatonGrammarParser.TransContext):
        self.transicoes.append(ctx.getText())
        pass

    def enterInicio(self, ctx:AutomatonGrammarParser.InicioContext):
        self.inicio = ctx.est().getText()
        pass

    def enterFinal(self, ctx:AutomatonGrammarParser.FinalContext):
        self.final = ctx.estado().getText().split(",")
        pass


    def visitErrorNode(self, node):
        print("Erro na entrada!!!!")
        exit(1);


def removeremetidos(lista):
    for i in lista:
        if i in lista:
            lista.remove(i)
    return lista


def main(argv):
    input = FileStream(argv[1])
    lexer = AutomatonGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AutomatonGrammarParser(stream)
    tree = parser.s()

    entrada = Automato()
    walker = ParseTreeWalker()
    walker.walk(entrada, tree)

    print("Alfabeto: ")
    print(entrada.alfabeto)

    print("Estados: ")
    print(entrada.estados)

    entrada.transicoes = entrada.transicoes[0].replace(",(", ";(").split(";")
    for cont in range(len(entrada.transicoes)):
        entrada.transicoes[cont] = entrada.transicoes[cont].replace("(", "")
        entrada.transicoes[cont] = entrada.transicoes[cont].replace(")", "")
        entrada.transicoes[cont] = entrada.transicoes[cont].replace("=", ",")
        entrada.transicoes[cont] = entrada.transicoes[cont].split(",")
    print("Transicoes: ")
    print(entrada.transicoes)

    print("Inicio: ")
    print(entrada.inicio)

    print("Finais: ")
    print(entrada.final)
if __name__ == '__main__':
    main(sys.argv)
