import sys
import inicio

class Game:

    def jogo():

        print('JOGO INICIADO - ADIVINHAÇÃO')
        tentativas = 3
        loop = False
        ini = inicio.Comeco

        while loop == False:

            while tentativas != 0 :

                
                A = int(input('Digite um numero entre 1 a 900: '))
                if A > 900 or A < 1:
                    print('****Entrada de Valores Errada****')
                elif A <= 599:
                    print('Está Muito Gelado')
                elif A >= 600 and A <= 750:
                    print('Está Gelado')
                elif A >= 751 and A <= 850:
                    print('Está Quente')
                elif A >= 851 and A <= 899:
                    print('Está Muito Quente')
                elif A == 900:
                    print('PARABENS VC ACERTOU!!!!')
                    break

                tentativas -= 1            
                print('\n{} tentativas sobrando' .format(tentativas))
            
            recebe = int(input("\nDigite \n1 para jogar novamente\n 2 Para encerrar\n 3 Para voltar a tela de Login:\t"))    
            if recebe == 1:
                tentativas = 3
            elif recebe == 2:
                print("Programa Finalizado")
                sys.exit()
            elif recebe == 3:
                ini.principal() 