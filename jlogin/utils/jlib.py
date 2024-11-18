'''
Importações do modulo os.path que lida com caminhos de diretorios e arquivos
isfile -> Verificar se um arquivo já existe
dump -> Escrever dados no formato json em um arquivo
'''
from os.path import isfile 
from json import dump, load


class JsonManager:

    def create_json(self, filepath, *args): # args -> Permite passar nº argumentos
        ''' Metodo responsavel por:
        -> Receber o nome do arquivo como argumento.
        -> Define um dicionario chamado "data" contendo duas chaves.
        '''
        data = {"username": "", "password": ""} # As chaves do dicionario
        if args:
            data = {"username": f"{args[0]}", "password": f"{args[1]}"}
    
        with open(filepath, "w") as f: 
            dump(data, f, indent=2, separators=(',', ': '))


    def read_json(self, filepath):
        ''' Metodo responsavel por:
        --> Ler um arquivo Json.
        --> Verifica se arquivo existe.
        '''
        if isfile(filepath):
            '''
                O metodo o open() abre o arquivo leitura. Por padrão, ele abre em modo leitura não é necessario para "r" no segundo parametro.
                "data" -> Recebe o conteudo do arquivo carregado pela função "load(f)", que le o arquivo na qual foi declarada como "f", e converte o conteudo JSON do arquivo para um objeto Python. 
            '''
            with open(filepath) as f:
                data = load(f)
            return data
        else:
            return False


    def update_json(self, filepath, data):
        with open(filepath, "w") as f: 
            dump(data, f, indent=2, separators=(',', ': '))
