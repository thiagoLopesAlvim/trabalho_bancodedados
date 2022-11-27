import pandas as pd
from model.vendedores import vendedores
from conexion.mongo_queries import MongoQueries

class Controller_Vendedor:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_vendedor(self) -> vendedores:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuario o novo CNPJ
        cpf = input("CPF (Novo): ")

        if self.verifica_existencia_vendedor(cpf):
            # Solicita ao usuario a nova razão social
            nome = input("Nome (Novo): ")
            # Solicita ao usuario o novo nome fantasia
            dt_contrat = input("Data de contratação (Novo): ")
            # Insere e persiste o novo fornecedor
            self.mongo.db["vendedores"].insert_one({"cpf": cpf, "nome": nome, "dt_contrat": dt_contrat})
            # Recupera os dados do novo fornecedor criado transformando em um DataFrame
            df_vendedor = self.recupera_vendedor(cpf)
            # Cria um novo objeto fornecedor
            novo_vendedor = vendedores(df_vendedor.cpf.values[0], df_vendedor.nome.values[0], df_vendedor.dt_contrat.values[0])
            # Exibe os atributos do novo fornecedor
            print(novo_vendedor.to_string())
            self.mongo.close()
            # Retorna o objeto novo_fornecedor para utilização posterior, caso necessário
            return novo_vendedor
        else:
            self.mongo.close()
            print(f"O CPF {cpf} já está cadastrado.")
            return None

    def atualizar_vendedor(self) -> vendedores:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do fornecedor a ser alterado
        cpf = int(input("CPF do fornecedor que deseja atualizar: "))

        # Verifica se o fornecedor existe na base de dados
        if not self.verifica_existencia_vendedor(cpf):
            # Solicita ao usuario a nova razão social
            nome = input("Nome (Novo): ")
            # Solicita ao usuario o novo nome fantasia
            dt_contrat = input("Data de contratação (Novo): ")            
            # Atualiza o nome do fornecedor existente
            self.mongo.db["vendedores"].update_one({"cpf":f"{cpf}"},{"$set": {"nome":nome, "dt_contrat":dt_contrat}})
            # Recupera os dados do novo fornecedor criado transformando em um DataFrame
            df_vendedor = self.recupera_vendedor(cpf)
            # Cria um novo objeto fornecedor
            vendedor_atualizado = vendedores(df_vendedor.cpf.values[0], df_vendedor.nome.values[0], df_vendedor.dt_contrat.values[0])
            # Exibe os atributos do novo fornecedor
            print(vendedor_atualizado.to_string())
            self.mongo.close()
            # Retorna o objeto fornecedor_atualizado para utilização posterior, caso necessário
            return vendedor_atualizado
        else:
            self.mongo.close()
            print(f"O CPF {cpf} não existe.")
            return None

    def excluir_vendedor(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o CPF do fornecedor a ser alterado
        cpf = int(input("CPF do fornecedor que irá excluir: "))        

        # Verifica se o fornecedor existe na base de dados
        if not self.verifica_existencia_vendedor(cpf):            
            # Recupera os dados do novo fornecedor criado transformando em um DataFrame
            df_fornecedor = self.recupera_vendedor(cpf)
            # Revome o fornecedor da tabela
            self.mongo.db["vendedores"].delete_one({"cpf":f"{cpf}"})
            # Cria um novo objeto fornecedor para informar que foi removido
            vendedor_excluido = vendedores(df_fornecedor.cpf.values[0], df_fornecedor.nome.values[0], df_fornecedor.dt_contrat.values[0])
            self.mongo.close()
            # Exibe os atributos do fornecedor excluído
            print("fornecedor Removido com Sucesso!")
            print(vendedor_excluido.to_string())
        else:
            self.mongo.close()
            print(f"O CPF {cpf} não existe.")

    def verifica_existencia_vendedor(self, cpf:str=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo fornecedor criado transformando em um DataFrame
        df_fornecedor = pd.DataFrame(self.mongo.db["vendedores"].find({"cpf":f"{cpf}"}, {"cpf": 1, "nome": 1, "dt_contrat": 1, "_id": 0}))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_fornecedor.empty

    def recupera_vendedor(self, cpf:str=None, external:bool=False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_cliente = pd.DataFrame(list(self.mongo.db["vendedores"].find({"cpf":f"{cpf}"}, {"cpf": 1, "nome": 1, "dt_contrat": 1, "_id": 0})))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_cliente