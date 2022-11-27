class Produto:
    def __init__(self, 
                 codigo_produto:int=None, 
                 nome_produto:str=None
                 ):
        self.set_codigo(codigo_produto)
        self.set_nome(nome_produto)

    def set_codigo(self, codigo:int):
        self.codigo_produto = codigo

    def set_nome(self, nome:str):
        self.nome_produto = nome

    def get_codigo(self) -> int:
        return self.codigo_produto

    def get_nome(self) -> str:
        return self.nome_produto

    def to_string(self) -> str:
        return f"Codigo: {self.get_codigo()} | Nome: {self.get_nome()}"