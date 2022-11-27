import pandas as pd
from bson import ObjectId

from reports.relatorios import Relatorio

from model.venda import Venda
from model.clientes import Cliente
from model.vendedores import vendedores
from model.produtos import Produto

from controller.controller_cliente import Controller_Cliente
from controller.controller_vendedor import Controller_Vendedor
from controller.controller_produto import Controller_Produto

from conexion.mongo_queries import MongoQueries
from datetime import datetime

class Controller_Venda:
    def __init__(self):
        self.ctrl_cliente = Controller_Cliente()
        self.ctrl_vendedor = Controller_Vendedor()
        self.ctrl_produto = Controller_Produto()
        self.mongo = MongoQueries()
        self.relatorio = Relatorio()
        
    def inserir_venda(self) -> Venda:
        # Cria uma nova conexão com o banco
        self.mongo.connect()
        
        # Lista os clientes existentes para inserir no pedido
        self.relatorio.get_relatorio_clientes()
        cpf = str(input("Digite o número do CPF do Cliente: "))
        cliente = self.valida_cliente(cpf)
        if cliente == None:
            return None

        # Lista os fornecedores existentes para inserir no pedido
        self.relatorio.get_relatorio_vendedores()
        cpfV = str(input("Digite o CPF do Vendedor: "))
        vendedor = self.valida_vendedor(cpfV)
        if vendedor == None:
            return None
        
        self.relatorio.get_relatorio_produtos()
        codigoP = int(input("Digite o código do produto"))
        produto = self.valida_produto(codigoP)
        if produto == None:
            return None

        data_hoje = datetime.today().strftime("%m-%d-%Y")
        proximo_venda = self.mongo.db["vendas"].aggregate([
                                                            {
                                                                '$group': {
                                                                    '_id': '$vendas', 
                                                                    'proximo_venda': {
                                                                        '$max': '$codigo_venda'
                                                                    }
                                                                }
                                                            }, {
                                                                '$project': {
                                                                    'proximo_venda': {
                                                                        '$sum': [
                                                                            '$proximo_venda', 1
                                                                        ]
                                                                    }, 
                                                                    '_id': 0
                                                                }
                                                            }
                                                        ])
        proximo_venda = int(list(proximo_venda)[0]['proximo_venda'])
        # Cria um dicionário para mapear as variáveis de entrada e saída
        #data = dict(codigo_venda=proximo_venda, data_pedido=data_hoje, cpf=cliente.get_CPF(), cpfV=vendedor.get_cpf(),codigo_produto = produto.get_codigo())
        # Insere e Recupera o código do novo pedido
        id_venda = self.mongo.db["vendas"].insert_one({"codigo_venda": proximo_venda,"data_pedido" : data_hoje ,"cpf": cliente.get_CPF(), "cpfV": vendedor.get_cpf(), "codigo_produto":produto.get_codigo()})
        # Recupera os dados do novo produto criado transformando em um DataFrame
        df_venda = self.recupera_venda(id_venda.inserted_id)
        # Cria um novo objeto Produto
        novo_venda = Venda(df_venda.codigo_venda.values[0], df_venda.data_venda.values[0], cliente, vendedor,produto)
        # Exibe os atributos do novo produto
        print(novo_venda.to_string())
        self.mongo.close()
        # Retorna o objeto novo_pedido para utilização posterior, caso necessário
        return novo_venda

    def atualizar_venda(self) -> Venda:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_venda = int(input("Código da Venda que irá alterar: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_venda(codigo_venda):

            # Lista os clientes existentes para inserir no pedido
            self.relatorio.get_relatorio_clientes()
            cpf = str(input("Digite o número do CPF do Cliente: "))
            cliente = self.valida_cliente(cpf)
            if cliente == None:
                return None

            # Lista os fornecedores existentes para inserir no pedido
            self.relatorio.get_relatorio_vendedores()
            cpfV = str(input("Digite o número do CPF do Vendedor: "))
            vendedor = self.valida_vendedor(cpfV)
            if vendedor == None:
                return None

            self.relatorio.get_relatorio_produtos()
            produtoC = int(input("Digite o codigo do produto: "))
            produto = self.valida_produto(produtoC)
            if produto == None:
                return None
            
            data_hoje = datetime.today().strftime("%m-%d-%Y")

            # Atualiza a descrição do produto existente
            self.mongo.db["vendas"].update_one({"codigo_pedido": codigo_venda}, 
                                                {"$set": {"cpfV": f'{vendedor.get_cpf()}',
                                                          "cpf":  f'{cliente.get_CPF()}',
                                                          "data_pedido": data_hoje,
                                                          "produto": f"{produto.get_codigo()}"
                                                          }
                                                })
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_pedido = self.recupera_venda_codigo(codigo_venda)
            # Cria um novo objeto Produto
            venda_atualizado = Venda(df_pedido.codigo_pedido.values[0], df_pedido.data_pedido.values[0], cliente, vendedor,produto)
            # Exibe os atributos do novo produto
            print(venda_atualizado.to_string())
            self.mongo.close()
            # Retorna o objeto pedido_atualizado para utilização posterior, caso necessário
            return venda_atualizado
        else:
            self.mongo.close()
            print(f"O código {codigo_venda} não existe.")
            return None

    def excluir_venda(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_venda = int(input("Código do Venda que irá excluir: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_venda(codigo_venda):            
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_venda = self.recupera_venda_codigo(codigo_venda)
            cliente = self.valida_cliente(df_venda.cpf.values[0])
            fornecedor = self.valida_vendedor(df_venda.cpfV.values[0])
            produto = self.valida_produto(df_venda.codigo_produto.values[0])
            
            opcao_excluir = input(f"Tem certeza que deseja excluir a venda {codigo_venda} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                print("Atenção, caso o pedido possua itens, também serão excluídos!")
                opcao_excluir = input(f"Tem certeza que deseja excluir o pedido {codigo_venda} [S ou N]: ")
                if opcao_excluir.lower() == "s":
                   
                    self.mongo.db["vendas"].delete_one({"codigo_venda": codigo_venda})
                    # Cria um novo objeto Produto para informar que foi removido
                    venda_excluido = Venda(df_venda.codigo_venda.values[0], df_venda.data_pedido.values[0], cliente, fornecedor,produto)
                    self.mongo.close()
                    # Exibe os atributos do produto excluído
                    print("Pedido Removido com Sucesso!")
                    print(venda_excluido.to_string())
        else:
            self.mongo.close()
            print(f"O código {codigo_venda} não existe.")

    def verifica_existencia_venda(self, codigo:int=None, external: bool = False) -> bool:
        # Recupera os dados do novo pedido criado transformando em um DataFrame
        df_venda = self.recupera_venda_codigo(codigo=codigo, external=external)
        return df_venda.empty

    def recupera_venda(self, _id:ObjectId=None) -> bool:
        # Recupera os dados do novo pedido criado transformando em um DataFrame
        df_venda = pd.DataFrame(list(self.mongo.db["vendas"].find({"_id":_id}, {"codigo_venda": 1, "data_venda": 1, "cpf": 1, "cpfV": 1, "pruduto":1,"_id": 0})))
        return df_venda

    def recupera_venda_codigo(self, codigo:int=None, external: bool = False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo pedido criado transformando em um DataFrame
        df_venda = pd.DataFrame(list(self.mongo.db["pedidos"].find({"codigo_pedido": codigo}, {"codigo_pedido": 1, "data_pedido": 1, "cpf": 1, "cpfV": 1,"codigo_produto":1, "_id": 0})))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_venda

    def valida_cliente(self, cpf:str=None) -> Cliente:
        if self.ctrl_cliente.verifica_existencia_cliente(cpf=cpf, external=True):
            print(f"O CPF {cpf} informado não existe na base.")
            return None
        else:
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_cliente = self.ctrl_cliente.recupera_cliente(cpf=cpf, external=True)
            # Cria um novo objeto cliente
            cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0])
            return cliente

    def valida_produto(self, codigo:str=None) -> Produto:
        if self.ctrl_produto.verifica_existencia_produto(codigo=codigo, external=True):
            print(f"O Código {codigo} do produto informado não existe na base;")
            return None
        else:
            df_produto = self.ctrl_produto.recupera_produto_codigo(codigo=codigo, external=True)
            produto = Produto(df_produto.codigo_produto.values[0], df_produto.nome_produto.values[0])
            return produto
        
    def valida_vendedor(self, cpfj:str=None) -> vendedores:
        if self.ctrl_vendedor.verifica_existencia_vendedor(cpfj, external=True):
            print(f"O CPF {cpfj} informado não existe na base.")
            return None
        else:
            # Recupera os dados do novo fornecedor criado transformando em um DataFrame
            df_vendedor = self.ctrl_vendedor.recupera_vendedor(cpfj, external=True)
            # Cria um novo objeto fornecedor
            vendedor = vendedores(df_vendedor.cpf.values[0], df_vendedor.nome.values[0], df_vendedor.dt_contrat.values[0])
            return vendedor