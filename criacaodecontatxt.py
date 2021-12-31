import sys
from typing import Text
import inicio

class CriarConta:
    

    def criar(): 
        
        usernew = input("\nDigite um nome de Usuario valido:  ")
        keynew = input("\nDigite um nome de Senha valida:  ")
       
        arq = open("log.txt","a")
        arq.write("\n")
        adds = [usernew, keynew, "0000"]
        
        for add in adds:
            arq.write(add)
            arq.write(" ")
        arq.close()
        
        print("\nCaso queira voltar a tela de login digite 1\n",
             "Caso queira sair digite 2")
        decisao = int(input("\nDigite a Opção:  "))
        
        if decisao == 1:
            ini = inicio.Comeco
            ini.principal()
        elif decisao ==2:
            sys.exit()     