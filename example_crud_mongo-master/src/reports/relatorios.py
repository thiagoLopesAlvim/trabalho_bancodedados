from conexion.mongo_queries import MongoQueries
import pandas as pd
from pymongo import ASCENDING, DESCENDING

class Relatorio:
    def __init__(self):
        pass

    

    def get_relatorio_produtos(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["produtos"].find({}, 
                                                 {"codigo_produto": 1, 
                                                  "nome_produto": 1, 
                                                  "_id": 0
                                                 }).sort("nome_produto", ASCENDING)
        df_produto = pd.DataFrame(list(query_result))
        # Fecha a conexão com o Mongo
        mongo.close()
        # Exibe o resultado
        print(df_produto)        
        input("Pressione Enter para Sair do Relatório de Produtos")

    def get_relatorio_clientes(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["clientes"].find({}, 
                                                 {"cpf": 1, 
                                                  "nome": 1, 
                                                  "telefone":1,
                                                  "dt_nascimento":1,
                                                  "_id": 0
                                                 }).sort("nome", ASCENDING)
        df_cliente = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_cliente)
        input("Pressione Enter para Sair do Relatório de Clientes")

    def get_relatorio_vendedores(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["vendedores"].find({}, 
                                                     {"cpf": 1, 
                                                      "nome": 1, 
                                                      "dt_contrat": 1, 
                                                      "_id": 0
                                                     }).sort("nome", ASCENDING)
        df_fornecedor = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_fornecedor)        
        input("Pressione Enter para Sair do Relatório de vendedores")

    def get_relatorio_vendas(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["vendas"].find({}, 
                                                     {"codigo_venda": 1, 
                                                      "data_venda": 1, 
                                                      "cpf": 1,
                                                      "cpfV":1,
                                                      "codigo_produto":1,
                                                      "_id": 0
                                                     }).sort("nome", ASCENDING)
        df_vendas = pd.DataFrame(list(query_result))
        # Fecha a conexão com o Mongo
        mongo.close()
        print(df_vendas)
        input("Pressione Enter para Sair do Relatório de Pedidos")
    
    