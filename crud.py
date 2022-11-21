from gridfs import ClientSession
import pymongo

mongo_cliente = pymongo.MongoClient(f"mongodb://labdatabase:labDatabase2022@localhost:27017/")


my_db = mongo_cliente["labdatabase"]
my_collection_v = my_db["Vendas"]
my_collection_c = my_db["Clientes"]
my_collection_ven = my_db["Vendedor"]
my_collection_pro = my_db["Produtos"]
total_vendas = my_collection_v.count_documents
total_clientes = my_collection_c.count_documents
total_vendedores = my_collection_ven.count_documents
total_produtos = my_collection_pro.count_documents
selecao = 0
while selecao != 5:
    print(f'''
        PROGRAMA DE VENDAS BANCO DE DADOS
        1-VENDAS: {total_vendas}
        2-CLIENTES: {total_clientes}
        3-VENDEDORES: {total_vendedores}
        4-Produtos: {total_produtos}


        1- Inserir
        2- Atualizar
        3- Deletar
        4- Relátorios
        5- Sair\n
        '''
    )
    selecao = int(input('Digite um valor para selecionar ação'))

    print(f'''
            1- Vendas
            2-Clientes
            3-Vendedores
            4-Produtos
        ''')

    selecao2= int(input("Digite um valor para decider qual tio de dado trabalhar\n"))
    if selecao == 1:
        if selecao2 ==1:
            id_v= input("Digite um ID para a venda\n")
            data_v= input("Data da venda \n")
            vendedor_v= input("digite o id do vendedor\n")
            Client_v= input("Digite o id do cliente\n")
            produto_v = input("Digite o id do produto\n")
            my_document_v = {f"id":{id_v},"data_venda":{data_v},"id_vendedor":{vendedor_v},"id_cliente":{Client_v},"id_produto":{produto_v}}
            my_collection_v.insert_one(my_document_v)
        if selecao2 == 2:
            id_v=input("Digite o id do Cliente")
            nome_c= input("Digite o nome do cliente")
            cpf_c= input("Digite o telefone do cliente")
            nascimento_c =input("Dgite a data de nascimento do cliente")
            my_document_c = {f"id":{id_v}, "nome":{nome_c}, "cpf": {cpf_c},"telefone":"","dt_nascimento":{nascimento_c}}
            my_collection_c.insert_one(my_document_c)
        if selecao2 == 3:
            id_ven = input("Digite um ID para o vendedor")
            nome_ven= input("Digite o nome do vendedor")
            cpf_ven = input("Digite o Cpf do vendedor")
            dt_contrat_ven = ("Digite a data de nascimento do vendedor")
            my_document_ven = {f"_id":{id_ven},"nome":{nome_ven},"cpf":{cpf_ven},"dt_contrat":{dt_contrat_ven}}
        if selecao2 == 4:
            id_p = input("Digite o Id do produto")
            nome_p= input("Gigite o Nome do produto")
            data_p = input("Dgite a data de validade do produto")
            my_document_pro = {f"id":{id_p},"nome":{nome_p},"data_validade":{data_p}}
            my_collection_pro.insert_one(my_document_pro)
    if selecao ==2:
        print()
    if selecao ==3:
        id_del = int(input('Digite o ID para qual deseja deletar o registro:'))
        if selecao2 == 1:
            my_collection_v.delete_one(f"id : {id_del}")
        if selecao2 == 2:
            my_collection_c.delete_one(f"id : {id_del}")
        if selecao2 == 3:
            my_collection_ven.delete_one(f"id : {id_del}")
        if selecao2 == 4:
            my_collection_pro.delete_one(f"id : {id_del}")
    if selecao == 4:
        if selecao2 == 1:
            print (my_collection_v.find(""))
        if selecao2 == 2:
            print(my_collection_c.find(""))
        if selecao2 == 3:
            print(my_collection_ven.find(""))
        if selecao2 == 4:
            print(my_collection_pro.find(""))
    if selecao == 5:
        exit
        
