from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_produto import Controller_Produto
from controller.controller_cliente import Controller_Cliente
from controller.controller_vendedor import Controller_Vendedor
from controller.controller_venda import Controller_Venda

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_produto = Controller_Produto()
ctrl_cliente = Controller_Cliente()
ctrl_vendedor = Controller_Vendedor()
ctrl_venda = Controller_Venda()

def reports(opcao_relatorio:int=0):

           
    if opcao_relatorio == 1:
        relatorio.get_relatorio_vendas()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_produtos()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_clientes()
    elif opcao_relatorio == 5:
        relatorio.get_relatorio_vendedores()

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_produto = ctrl_produto.inserir_produto()
    elif opcao_inserir == 2:
        novo_cliente = ctrl_cliente.inserir_cliente()
    elif opcao_inserir == 3:
        novo_fornecedor = ctrl_vendedor.inserir_vendedor()
    elif opcao_inserir == 4:
        novo_pedido = ctrl_venda.inserir_venda()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_produtos()
        produto_atualizado = ctrl_produto.atualizar_produto()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_clientes()
        cliente_atualizado = ctrl_cliente.atualizar_cliente()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_vendedores()
        fornecedor_atualizado = ctrl_vendedor.atualizar_vendedor()
    elif opcao_atualizar == 4:
        relatorio.get_relatorio_vendas()
        pedido_atualizado = ctrl_venda.atualizar_venda()

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_produtos()
        ctrl_produto.excluir_produto()
    elif opcao_excluir == 2:                
        relatorio.get_relatorio_clientes()
        ctrl_cliente.excluir_cliente()
    elif opcao_excluir == 3:                
        relatorio.get_relatorio_vendedores()
        ctrl_vendedor.excluir_vendedor()
    elif opcao_excluir == 4:                
        relatorio.get_relatorio_vendas()
        ctrl_venda.excluir_venda()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-4]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-5]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-4]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-4]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-4]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()