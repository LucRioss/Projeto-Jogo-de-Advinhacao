import sys
import inicio 
from game import Game
from typing import Text


class EntrarNaConta:
    def login():
        game = Game
        ini = inicio.Comeco
        
        while True:    
            user = input('\nDigite o Usuário:\t')
            key = input('Dgite a Senha:\t')
            arquivotxt = open("log.txt","r")

            for linha in arquivotxt:
                valores = linha.split()

                if  user == valores[0] and key == valores[1]:
                    print('\nAcesso Concedido')
                    game.jogo()               
                    break  
                elif user != valores[0] or key != valores[1]:                   
                    print("")
                    print('\n********Acesso Negado********')
                    sair = int(input("\nPara Voltar a Tela de Inicio DIGITE 1 ou 0 Para Encerrar o Programa:  "))
                   
                    if sair == 1:
                        ini.principal()
                    elif sair == 0:
                        sys.exit()

            arquivotxt.close()