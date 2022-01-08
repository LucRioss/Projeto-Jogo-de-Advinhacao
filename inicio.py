import sys
from criacaodecontatxt import CriarConta
from login import EntrarNaConta
#match-case-python-disponivel-na-versão-3.10-versão-utilizada-para-a-criação-desse-codigo-está-na-3.7



class Comeco:
    def principal():
        print('\n','------------BEM VINDO-----------', '\n', 'Selecione uma das Opções Abaixo:', '\n', '-'*32, '\n')
        print(' 1 Para Entrar em uma Conta já Existente.' ,'\n', '2 Para Criar uma Nova Conta.','\n','0 Para Encerrar o Programa')
        selecionar = int(input(' Digite a opção desejada: '))

        while True:            

            if selecionar == 1:
                EntrarNaConta.login()
            elif selecionar == 2:
                CriarConta.criar()
            elif selecionar == 0:
                print('\n')
                print('-='*20)
                print('\tPrograma Encerrado')
                print('-='*20)
                sys.exit()
            elif selecionar !=1 or selecionar != 2 or selecionar != 0:
                parada = int(input('\nOpção não encontrada, Por Favor digite novamente:\t'))
                selecionar = parada
            

