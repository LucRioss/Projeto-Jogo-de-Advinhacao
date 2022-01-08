import sys
import inicio

class Game:

    def jogo():

        print('JOGO INICIADO - ADIVINHAÇÃO')
        tentativas = 3
        #loop = False
        ini = inicio.Comeco

        while True:

            while tentativas != 0 :
               
                A = int(input('\nDigite um número entre 1 a 900: '))
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
                    print('ENCONTROU PARABÉNS!!!')
                    break

                tentativas -= 1            
                print('\n{} tentativas sobrando' .format(tentativas))
            
            print('\n',
            '---------Opções--------','\n',
            '1 Para Jogar Novamente','\n',
            '2 Para Encerrar o Programa','\n',
            '3 Para Voltar a tela de Login\t')
            valida = int(input((' Digite:')))    
            
            if valida == 1:
                tentativas = 3
            elif valida == 2:
                print('\n------Programa Finalizado--------')
                sys.exit()
            elif valida == 3:
                ini.principal()
