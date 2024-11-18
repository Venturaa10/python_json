from os.path import dirname, realpath, join
from utils.jlib import JsonManager
''' Modulos importados para manipulação e verificação de senhas.
run -> pip install passlib
 '''
from getpass import getpass
from passlib.hash import pbkdf2_sha256

class Jlogin(JsonManager):
    def __init__(self):
        self.root = dirname(realpath(__file__))
        self.path_data = join(self.root, 'data/data.json')

    def sign_in(self):
        '''
        Metodo responsavel por:
        -> Solicitar nome de usuario e a senha do usuario.
        -> "getpass" -> Permite que a senha não esteja visivel durante a digitação.
        -> Verificar se as senhas digitadas coincidem
        -> Após validação, é criado um arquivo JSON com o username e o hash da senha (gerar uma senha segura) gerada com "pbkdf2_sha256".
        '''
        # data = JsonManager().read_json(self.path_data)
        print('### Sing In ###')
        username = input('Enter your username: ')
        # Solicitar senha invisivel durante a digitação
        password = getpass('Enter your password: ') 
        password_verify = getpass('Repeat your password: ')

        while password != password_verify:
            print('Password do not match!')
            password_verify = getpass('Repeat your password: ')

        # Criar um arquivo JSON com o username e hash da senha
        JsonManager().create_json(self.path_data, username, pbkdf2_sha256.hash(password_verify)) 
        print(f'Username Created: {username}')


    def logging_in(self, data):
        ''' Metodo responsavel por:
        -> Solicitar nome de usuario e verificar se corresponde ao esperado no dicionario "data".
        -> Solicitar a senha e fazer a comparação com o hash armazenado utilizando o metodo "verify"
        -> "verify" parametros:
        1º: Senha fornecida pelo usuario (em texto simples).
        2º: O hash armazenado associado a senha original.
        -> Se as senhas não coincidirem, informa senha invalida. Se não, login efetuado com sucesso.
        '''
        print('### Loggin In ###')
        username = input('Enter your username: ')
        while username != data['username']:
            print('Username Invalid!')
            username = input('Enter your username: ')

        password = getpass('Enter your password: ') 
        # Verificar senhas com hash
        if not pbkdf2_sha256.verify(password, data['password']):
            print('Password Invalid!')

        else: 
            print('Login Success!')

    def main(self):
        data = JsonManager().read_json(self.path_data)
        if data: # Se o arquivo for lido corretamente (ou seja, "data" não for vazio), entra na condição para efetuar o login.
            self.logging_in(data)

        # self.sign_in()

if __name__ == '__main__':
    jl = Jlogin()
    jl.main()