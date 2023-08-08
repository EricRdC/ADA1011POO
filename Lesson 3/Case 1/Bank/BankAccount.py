class Conta:
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def __repr__(self):
        return f"Conta(numero='{self.numero}', saldo='{self.saldo}', cliente='{self.cliente}')"