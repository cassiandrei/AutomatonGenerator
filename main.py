import sys

from antlr4 import *

from antlr.AutomatonGrammarLexer import AutomatonGrammarLexer
from antlr.AutomatonGrammarParser import AutomatonGrammarParser
from antlr.AutomatonGrammarListener import AutomatonGrammarListener


class Automato(AutomatonGrammarListener):
    alfabeto = []
    estados = []
    transicoes = []

    def enterAlf(self, ctx:AutomatonGrammarParser.AlfContext):
        self.alfabeto.append(ctx.letra().getText())
        pass

    def enterEstados(self, ctx:AutomatonGrammarParser.EstadosContext):
        self.estados.append(ctx.estado().getText())
        pass

    def enterTrans(self, ctx:AutomatonGrammarParser.TransContext):
        self.transicoes.append(ctx.getText())
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
        entrada.transicoes[cont] = entrada.transicoes[cont].replace("(","")
        entrada.transicoes[cont] = entrada.transicoes[cont].replace(")", "")
        entrada.transicoes[cont] = entrada.transicoes[cont].replace("=", ",")
        entrada.transicoes[cont] = entrada.transicoes[cont].split(",")
    print("Transicoes: ")
    print(entrada.transicoes)

if __name__ == '__main__':
    main(sys.argv)
