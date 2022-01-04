import sys
from criacaodecontatxt import CriarConta
from login import EntrarNaConta
#match-case-python-disponivel-na-versão-3.10-versão-utilizada-para-a-criação-desse-codigo-está-na-3.7



class Comeco:
    def principal():

        loop = True

        print("\n------------BEM VINDO-----------","\n","Selecione uma das opções Abaixo:","\n")
        print("1 Para entrar em uma conta já existente." ,"\n", "2 Para criar uma nova conta.")
        selecionar = int(input("Digite a opção desejada: "))
        

        while loop == True:            

            if selecionar == 1:
                EntrarNaConta.login()
            elif selecionar == 2:
                CriarConta.criar()
            elif selecionar == 0:
                print("\nPrograma Encerrado\n")
                loop = False
            elif selecionar !=1 or selecionar != 2 or selecionar != 0:
                parada = int(input("\nOpção não encontrada, por favor digite novamente ou 0 para sair:  "))
                selecionar = parada
            

