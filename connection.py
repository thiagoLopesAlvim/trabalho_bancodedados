from http import client
import pymongo
from pyparsing import null_debug_action

client = pymongo.MongoClient(f"mongodb://labdatabase:labDatabase2022@localhost:27017/")
db = client.Cliente    
db2= client.Produtos
print(client.list_database_names)
opcao_i = -1
opcao= -1
qaunt_clientes= db.Cliente.count_documents()
quant_produtos = db2.Produtos.count_documents()
def menu():
    print(f"""
        MENU:
            SISTEMA DE VENDAS
            TOTAL DE REGISTROS EXISTENTES
            1- CLIENTES : {qaunt_clientes}
            2- PRODUTOS : {quant_produtos}

            ALTERNATIVAS:
            1-ISERIR DOCUMENTO
            2-REMOVER DOCUMENTOS
            3-ATUALIZAR DOCUMENTOS
            4-RELATORIOS

            CRIADO PRO: TIHAGO ALVIM

            DISCIPLINA: BANCO DE DADOS 2022-2
            PROFESSOR: HOWARD ROATTI
    """)
    opcao = int(input("Escolha uma opcao"))


def menu2():
    print(f""" 
        1- Clientes
        2- Produtos
    """)
    opcao_i= int(input("Esolha uma opção:"))



def insert():
    if(opcao_i == 1):
        id = int(input(" Digite um id"))
        nome = input("Nome do cliente")
        cpf= input("CPF do cliente")
        idade= int(input("Digite sua idade"))
        db.Cliente.insert_one(
            {
                "id" : id,
                "nome": nome,
                "CPF" : cpf,
                "Idade": idade
            }
        print("Dados inseridos com sucesso")
        )
    elif(opcao_i == 2):
        id = int(input(" Digite um id"))
        nome = input("Nome do produto")
        valor = input(" Valor do produto")
        db2.Produtos.insert_one(
            {
                "id": id,
                "nome": nome,
                "valor": valor
            }
        )


   