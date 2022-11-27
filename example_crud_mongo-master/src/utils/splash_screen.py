from utils import config

class SplashScreen:

    def __init__(self):
        # Nome(s) do(s) criador(es)
        self.created_by = """Thiago Augusto Lopes Alvim
                              Ezequiel Soeiro Gomes
                              Lucio Ribeiro dos Santos
                              Ronaldo Luiz de Almeida Junior
                              Nivaldo Gonçalves de Matos"""
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_documents_count(self, collection_name):
        # Retorna o total de registros computado pela query
        df = config.query_count(collection_name=collection_name)
        return df[f"total_{collection_name}"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - PRODUTOS:         {str(self.get_documents_count(collection_name="produtos")).rjust(5)}
        #      2 - CLIENTES:         {str(self.get_documents_count(collection_name="clientes")).rjust(5)}
        #      3 - VENDEDORES:     {str(self.get_documents_count(collection_name="vendedores")).rjust(5)}
        #      4 - VENDAS:          {str(self.get_documents_count(collection_name="vendas")).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """