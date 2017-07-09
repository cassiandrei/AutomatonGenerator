from estado import Estado

class Automato:
    definicao = None
    fita = ""
    estados = []
    atual = None

    def __init__(self, definicao, fita):
        self.definicao = definicao
        self.fita = fita
        self.geraEstados()
        self.geraFilhos()
        self.atual = self.getEstado(definicao.inicio)

    def geraEstados(self):
        for estado in self.definicao.estados:
            novoestado = Estado(estado)
            self.estados.append(novoestado)

    def getEstado(self, nome):
        for estado in self.estados:
            if estado.nome == nome:
                return estado
        print("ERRO: "+nome)

    def geraFilhos(self):
        for estado in self.estados:
            print(estado.nome)
            print(len(estado.filhos))
            for trans in self.definicao.transicoes:
                if trans[0] == estado.nome:
                    estado.addFilho(self.getEstado(trans[2]))

    def valida(self):
        if len(self.fita) > 0:
            token = self.fita[0]
            self.fita = self.fita[1:]
            print("teste: ")
            for filho in self.atual.filhos:
                print(self.atual.nome, filho.nome)
        else:
            if self.atual in self.definicao.final:
                return True
            else:
                return False



