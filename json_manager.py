'''
Importações do modulo os.path que lida com caminhos de diretorios e arquivos
isfile -> Verificar se um arquivo já existe
dump -> Escrever dados no formato json em um arquivo
'''

from os.path import dirname, realpath, isfile 

from json import dump


class JsonManager:

    def __init__(self):
        ''' Inicializa o caminho base do diretorio onde o script esta sendo executado e armazena em self.path.
        '''
        self.path = dirname(realpath(__file__)) + '/' 

    def create_json(self, file):
        ''' Metodo responsavel por:
        -> Receber o nome do arquivo como argumento.
        -> Define um dicionario chamado "data" contendo duas chaves.
        -> Combina o caminho base com o nome do arquivo para determinar o caminho completo onde o Json será criado 
        -> Verifica se o arquivo nesse caminho especificado já existe usando "not isfile"

        '''
        data = {"username": "", "password": ""} # As chaves do dicionario
        path_data_json = self.path + file 

        if not isfile(path_data_json):
            '''Se não existir, cria o arquivo JSON com os dados do dicionario e retorna True
            -> "with open" --> Parametros
            1º: caminho completo do arquivo.
            2º: "w" (write) indica que é para escrever(criar) esse arquivo.
            "f" -> O arquivo criado é referenciado pelo "f"
            '''
            with open(path_data_json, "w") as f:
                ''' dump -> Parametros
                1º: Os dados a serem convertidos em JSON, ou seja, o dicionario "data" nesse caso.
                2º: O arquivo onde os dados serão escritos ("f")
                3º: "indent" -> Quantidade de indentação
                4º: Ajusta como os elementos do JSON são formatados, a "," separa os itens, ":" separa as chaves e os valores.
                '''
                dump(data, f, indent=2, separators=(',', ': '))
            return True
        else:
            ''' Se já existir, não cria o arquivo'''
            return False

if __name__ == '__main__':
    jmanager = JsonManager()
    jmanager.create_json('data/data.json') # Caminho onde arquivo json vai ser criado
    