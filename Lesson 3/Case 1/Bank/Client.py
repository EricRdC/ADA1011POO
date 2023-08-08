class Cliente:
    def __init__(self, nome, sobrenome, CPF, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.CPF = CPF
        self.telefone = telefone

    def __repr__(self):
        return f"Cliente(nome='{self.nome}', sobrenome='{self.sobrenome}', CPF='{self.CPF}', telefone='{self.telefone}')"
