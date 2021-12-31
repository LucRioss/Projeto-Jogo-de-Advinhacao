import sys
from game import Game
from typing import Text
import inicio 

class EntrarNaConta:

    def login():
        game = Game
        ini = inicio.Comeco
        loop = False
        
        while loop == False:   
            
            user = input('\nDigite seu nome de usuario:  ')
            key = input('Dgite a sua senha:  ')
            
            arquivotxt = open("log.txt","r")

            for linha in arquivotxt:
                valores = linha.split()

                if  user == valores[0] and key == valores[1]:
                    print('\nAcesso Concedido')
                    loop = True
                    game.jogo()               
                    break
                
                elif user != valores[0] or key != valores[1]:                   
                    print("")
                    print('\n********Acesso Negado********')
                    sair = int(input("\nCaso queria voltar a tela de inicio precione 1 caso contrario digite 0:  "))
                   
                    if sair == 1:
                        ini.principal()
                    elif sair == 0:
                        break

        arquivotxt.close()