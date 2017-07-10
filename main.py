import sys

from antlr4 import *

from antlr.AutomatonGrammarLexer import AutomatonGrammarLexer
from antlr.AutomatonGrammarParser import AutomatonGrammarParser
from antlr.AutomatonGrammarListener import AutomatonGrammarListener
from automato import Automato


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
    fita = input("Digite a fita de definicao:")
    lexer = AutomatonGrammarLexer(arquivo)
    stream = CommonTokenStream(lexer)
    parser = AutomatonGrammarParser(stream)
    tree = parser.s()

    definicao = Listener()
    walker = ParseTreeWalker()
    walker.walk(definicao, tree)

    definicao.transicoes = definicao.transicoes[0].replace(",(", ";(").split(";")
    for cont in range(len(definicao.transicoes)):
        definicao.transicoes[cont] = definicao.transicoes[cont].replace("(", "")
        definicao.transicoes[cont] = definicao.transicoes[cont].replace(")", "")
        definicao.transicoes[cont] = definicao.transicoes[cont].replace("=", ",")
        definicao.transicoes[cont] = definicao.transicoes[cont].split(",")

    auto = Automato(definicao, fita)
    if auto.valida():
        print("Entrada RECONHECIDA")
    else:
        print("Entrada NAO RECONHECIDA")

if __name__ == '__main__':
    main()
