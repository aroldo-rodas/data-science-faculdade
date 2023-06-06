import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("data de abertura: {}".format(self.data_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-", t)
        

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = nome
        self.cpf = cpf

class Conta:
    #Construtor
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    
    #Deposita
    def deposito(self, valor):
        self.saldo += valor
    
    #Saca
    def saca(self, valor):
        self.saldo -= valor

    #Extrato
    def extratato(self):
        print("Número: {} e saldo: {}".format(self.numero, self.saldo))

    #Transfere
    def transfere(self, destino, valor):
       self.saldo -= valor
       destino.saldo += valor

def main():
    cliente1 = Cliente('Aroldo', 'Rodas Miranda Filho', '050.754.691-25')
    conta1 = Conta('123-4', cliente1, 120.0, 1000.0)
    #conta2 = Conta('999-9', 'Aroldo', 999.9, 9999.9)

    print(conta1.titular.nome)
    conta1.historico.imprime()

main()