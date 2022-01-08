import sys
from typing import Text
import inicio

class CriarConta:
    
    def criar(): 
        
        usernew = input("\nDigite o Nome de Usuário:\t")
        keynew = input("\nDigite a Senha:\t")
       
        arq = open("log.txt","a")
        arq.write("\n")
        adds = [usernew, keynew, "0000"]
        
        for add in adds:
            arq.write(add)
            arq.write(" ")
        arq.close()
        
        print('\n','-------Opções--------',
              '\n','1 Para Voltar a Tela de Login',
              '\n','2 Para Sair Digite')
        decisao = int(input("\nDigite a Opção:  "))
        print('-'*30)

        if decisao == 1:
            ini = inicio.Comeco
            ini.principal()
        elif decisao ==2:
            sys.exit()     