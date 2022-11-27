class Cliente:
    def __init__(self, 
                 CPF:str=None, 
                 nome:str=None,
                 telefone: str=None,
                 dt_nascimento: str=None
                ):
        self.set_CPF(CPF)
        self.set_nome(nome)
        self.set_telefone(telefone)
        self.set_dt_nascimento(dt_nascimento)

    def set_CPF(self, CPF:str):
        self.CPF = CPF

    def set_nome(self, nome:str):
        self.nome = nome
    
    def set_telefone(self, telefone: str):
        self.telefone = telefone
    
    def set_dt_nascimento(self, dt_nascimento:str):
        self.dt_nascimento = dt_nascimento 

    def get_CPF(self) -> str:
        return self.CPF

    def get_nome(self) -> str:
        return self.nome
    
    def get_telefone(self) -> str:
        return self.telefone
    def get_dt_nascimento(self) -> str:
        return self.dt_nascimento

    def to_string(self) -> str:
        return f"CPF: {self.get_CPF()} | Nome: {self.get_nome()} | Telefone: {self.get_telefone()} | Data de nascimento: {self.get_dt_nascimento()} "