class Estado:
    nome = ""
    filhos = []
    transacoes = []


    def __init__(self, nome):
        self.nome = nome

    def addFilho(self, filho):
        self.filhos.append(filho)

    def addTrans(self, transacao):
        self.transacoes.append(transacao)
