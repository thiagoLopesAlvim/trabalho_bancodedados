class vendedores:
    def __init__(self, 
                 nome: str=None,
                 cpf: str=None,
                 dt_contrat: str=None
                 ):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_dt_contrat(dt_contrat)

    def set_nome(self, nome:str):
        self.nome = nome

    def set_cpf(self, cpf:str):
        self.cpf = cpf

    def set_dt_contrat(self, dt_contrat:str):
        self.dt_contrat = dt_contrat

    def get_nome(self) -> str:
        return self.nome

    def get_cpf(self) -> str:
        return self.cpf

    def get_dt_contrat(self) -> str:
        return self.dt_contrat

    def to_string(self) -> str:
        return f"Nome: {self.get_nome()} | CPF: {self.get_cpf()} | Data de contratação: {self.get_dt_contrat()}"