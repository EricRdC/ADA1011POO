class Cliente:
    def __init__(self, nome, sobrenome, CPF, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.CPF = CPF
        self.telefone = telefone

    def __repr__(self):
        return f"Cliente(nome='{self.nome}', sobrenome='{self.sobrenome}', CPF='{self.CPF}', telefone='{self.telefone}')"

class Conta:
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def __repr__(self):
        return f"Conta(numero='{self.numero}', saldo='{self.saldo}', cliente='{self.cliente}')"

cliente = Cliente(nome="João", sobrenome="Silva", CPF="123.456.789-00", telefone="11999999999")
conta = Conta(numero="123456789", saldo=1000, cliente=cliente)

print(cliente)

print(conta)