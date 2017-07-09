import sys

from antlr4 import *

from antlr.AutomatonGrammarLexer import AutomatonGrammarLexer
from antlr.AutomatonGrammarParser import AutomatonGrammarParser
from antlr.AutomatonGrammarListener import AutomatonGrammarListener


class Listener(AutomatonGrammarListener):
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
        print("Erro na definição do automato!!!!")
        exit(1);


def removeremetidos(lista):
    for i in lista:
        if i in lista:
            lista.remove(i)
    return lista


def main():
    arquivo = FileStream("Automato.txt")
    fita = input("Digite a fita de entrada:")
    lexer = AutomatonGrammarLexer(arquivo)
    stream = CommonTokenStream(lexer)
    parser = AutomatonGrammarParser(stream)
    tree = parser.s()

    definicao = Listener()
    walker = ParseTreeWalker()
    walker.walk(definicao, tree)

    entrada.transicoes = entrada.transicoes[0].replace(",(", ";(").split(";")
    for cont in range(len(entrada.transicoes)):
        entrada.transicoes[cont] = entrada.transicoes[cont].replace("(", "")
        entrada.transicoes[cont] = entrada.transicoes[cont].replace(")", "")
        entrada.transicoes[cont] = entrada.transicoes[cont].replace("=", ",")
        entrada.transicoes[cont] = entrada.transicoes[cont].split(",")

    if Automato(definicao, fita):
        print("Entrada reconhecida pelo automato")
    else:
        print("Entrada nao reconhecida pelo automato")

if __name__ == '__main__':
    main()
