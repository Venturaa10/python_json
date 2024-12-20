'''
Importações do modulo os.path que lida com caminhos de diretorios e arquivos
isfile -> Verificar se um arquivo já existe
dump -> Escrever dados no formato json em um arquivo
'''
from os.path import isfile 
from json import dump, load


class JsonManager:

    def create_json(self, filepath, *args): # args -> Permite passar nº argumentos
        '''
        Cria um objeto Json.
        Argumentos: 
        - "filepath" -> Caminho do arquvio JSON.
        - "args" -> Permite receber mais argumentos se necessario.

        Variaveis:
        - "data" -> Define um dicionario contendo as chaves.

        Condição if "args":
        - Verifica se há argumetos passados como parametro.
        - if True, passa os argumentos como valores das chaves.

        with open(): 
        - Abre o arquivo no caminho "filepath" e o "w" indica que é para escrever(criar).
        - Referencia o arquivo escrito como "f".
        - "dump" -> Converte o objeto "data" para um string Json.
        '''

        data = {"username": "", "password": ""} # As chaves do dicionario
        if args:
            data = {"username": f"{args[0]}", "password": f"{args[1]}"}
    
        with open(filepath, "w") as f: 
            dump(data, f, indent=2, separators=(',', ': '))


    def read_json(self, filepath):
        ''' Metodo responsavel por:
        - Ler um arquivo Json.
        - Verifica se arquivo existe.
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
        ''' Metodo responsavel por:
        - Atualizar as informações de um arquivo JSON.
        Parametros: 
        - "filepath" -> Recebe o caminho do arquivo JSON que será atualizado.
        - "data" -> Recebe o objeto contendo os dados que serão escritos no arquivo JSON.

        --> Este metodo sobrescreve o conteúdo do arquivo com os dados fornecidos.
        '''
        with open(filepath, "w") as f: 
            dump(data, f, indent=2, separators=(',', ': '))
