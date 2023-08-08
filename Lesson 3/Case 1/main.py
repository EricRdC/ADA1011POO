from Bank import Cliente, Conta

cliente = Cliente(nome="João", sobrenome="Silva", CPF="123.456.789-00", telefone="11999999999")
conta = Conta(numero="123456789", saldo=1000, cliente=cliente)

print(cliente)

print(conta)
