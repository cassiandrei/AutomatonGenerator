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
        self.atual = self.getEstado(definicao.inicio)

    def geraEstados(self):
        for estado in self.definicao.estados:
            self.estados.append(Estado(estado))

    def getEstado(self, nome):
        for estado in self.estados:
            if estado.nome == nome:
                return estado
        print("ERRO: Estado inexistente " + nome)
        exit(1)

    def valida(self):
        print("Iniciando reconhecimento... Estado inicial: "+self.atual.nome)
        while len(self.fita) > 0:
            passou = False
            token = self.fita[0]
            if token not in self.definicao.alfabeto:
                print("TOKEN :"+token+" invalido ou fora do alfabeto")
                return False
            if len(self.fita) == 1:
                self.fita = ""
            else:
                self.fita = self.fita[1:]
            for trans in self.definicao.transicoes:
                if trans[0] == self.atual.nome and trans[1] == token:
                    print("Estado atual: " + self.atual.nome + " Token: " + token + " Transicao: " + trans[2])
                    self.atual = self.getEstado(trans[2])
                    passou = True
                    break
            if passou is False:
                print("Nao possui transicao do token: "+ token +" no estado: "+ self.atual.nome)
                return False
        if self.atual.nome in self.definicao.final:
            return True
        else:
            print("Fita vazia e estado atual nao eh FINAL")
            return False