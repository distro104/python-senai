
'''
'' EXERCICIO DE ESTUDO DAS ESTRUTURAS DE LOOP COM LIMITE DE REPETIÇÃO
'' 
'' 
''' 
import os
from time import sleep
import random

num_inicial = 1
num_final = 100
ultimo_numeros = []
em_jogo = False

#########################################################################
####   Define funções para o cabeçalho, rodapé, limpar tela e linha  ####
def cabecalho(Valor_min, Valor_max, ultimo_numeros=[]):
    limpar_tela()
    linha()
    texto_centralizado("ADIVINHE O NUMERO!")
    linha()
    print(f"Intervalo de números: {Valor_min} a {Valor_max}")
    print(f"Ultimas tentativas:")
    for numero in ultimo_numeros:
        print(f"{numero}", end=" ")
    print("\n")
    linha()
#######
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
#######
def linha(size=60):
    s = ''.join(['=' for x in range(size)])
    print(s)
#######
def texto_centralizado(texto, size=60):
    texto = texto.center(size)
    print(texto)
#########################################################################
def escolha_intervalo():
    global num_inicial, num_final
    while True:
        num_inicial = int(input("Digite o valor inicial do intervalo: "))
        num_final = int(input("Digite o valor final do intervalo: "))
        if num_inicial >= num_final:
            print("O valor inicial deve ser menor que o valor final. Tente novamente.")
        else:
            break
#########################################################################

######
def menu():
    while True:
        limpar_tela()
        if em_jogo:
            cabecalho(num_inicial, num_final, ultimo_numeros)
            print("1 - ESCOLHA O INTERVALO DOS NUMEROS:")
            print("2 - COMEÇAR O JOGO DE ADIVINHAÇÃO:")
            print("0 - FINALIZAR PROGRAMA...")
            linha()

            escolha = int(input("Escolha uma opção:"))
            match escolha:
                case 0:
                    print("\nFinalizando o programa...")
                    break
                case 1:
                    cabecalho(num_inicial, num_final, ultimo_numeros)
                case 2:
                    cabecalho()
        else:
            cabecalho(1,999,ultimo_numeros = [1,3,5,7,9])
            #cabecalho(Valor_min, Valor_max, ultimo_numeros=[]):
            escolha = int(input("Digite um numero:"))
            if escolha < num_inicial or escolha > num_final:
                print(f"Escolha um numero entre {num_inicial} e {num_final}.")
                escolha = None
            else:
                
# Executa o programa
if __name__ == "__main__":
    menu()