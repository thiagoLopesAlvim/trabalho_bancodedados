from datetime import date
from model.clientes import Cliente
from model.vendedores import vendedores
from model.produtos import Produto

class Venda:
    def __init__(self, 
                 codigo_venda:int=None,
                 data_venda:date=None,
                 cpf:Cliente= None,
                 cpfV:vendedores=None,
                 codigo_produto: Produto=None
                 ):
        self.set_codigo_venda(codigo_venda)
        self.set_data_venda(data_venda)
        self.set_cliente(cpf)
        self.set_vendedor(cpfV)
        self.set_produto(codigo_produto)


    def set_codigo_venda(self, codigo_venda:int):
        self.codigo_venda = codigo_venda

    def set_data_venda(self, data_venda:date):
        self.data_venda = data_venda

    def set_cliente(self, cliente:Cliente):
        self.cpf = cliente

    def set_vendedor(self, vendedor:vendedores):
        self.cpfV = vendedor

    def set_produto(self, produto:Produto):
        self.codigo_produto = produto

    def get_codigo_venda(self) -> int:
        return self.codigo_venda

    def get_data_venda(self) -> date:
        return self.data_venda

    def get_cliente(self) -> Cliente:
        return self.cpf

    def get_vendedor(self) -> vendedores:
        return self.cpfV
    

    def get_produto(self) -> Produto:
        return self.codigo_produto

    def to_string(self) -> str:
        return f"Venda: {self.get_codigo_venda()} | Data: {self.get_data_venda()} | Cliente: {self.get_cliente().get_nome()} | Vendedor: {self.get_vendedor().get_nome()} | Produto: {self.get_produto().get_nome()}"