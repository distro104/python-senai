'''
' EXERCICIO FEITO EM SALA DE AULA:
' PROGRAMA RESPONSAVEL POR FAZER O CALCULO DE 2 VALORES E EXIBI-LOS NA TELA
' DEVERA SER FEITO OS CALCULOS DE SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, E DIVISÃO
' E TAMBEM DEVE SER FEITO A VALIDAÇÃO SE CASO HAJA DIVISÃO POR 0. 
'''

import os

os.system('cls')

def tela(entrada_1, entrada_2, val_soma, val_mul, val_sub, val_div, div_zero):
    os.system('cls')
    print ("---------------------------------------------------------")
    print ("             Calculo de valores: RESULTADO")
    print ("---------------------------------------------------------")
    print (f"--------------------> Valor 1: {entrada_1} <---------------------")
    print (f"--------------------> Valor 2: {entrada_2} <---------------------")

    print (f"  Soma: {entrada_1} + {entrada_2} = {val_soma}")
    print (f"  Subtração: {entrada_1} - {entrada_2} = {val_sub}")
    print (f"  Multiplicação: {entrada_1} * {entrada_2} = {val_mul}")
    div_zero = (entrada_2 <= 0)
    if (div_zero):
        print(val_div)
    else:
        print(f"  Divisão: {entrada_1} / {entrada_2} = {val_div}")
    print("------------------ Programa finalizado -------------------")

entrada_1 = float(input("Digite o Primeiro valor:"))
entrada_2 = float(input("Digite o Segundo valor:"))

### Valores
val_soma = entrada_1 + entrada_2
val_mul = entrada_1 * entrada_2
val_sub = entrada_1 - entrada_2
div_zero = (entrada_2 <= 0)
if (div_zero):
    val_div = "  Divisão: O RESULTADO TEM DIVISÃO POR 0  E  NÃO PODE   SER\n           EXECUTADO!"
else:
    val_div = round((entrada_1 / entrada_2),1)

tela(entrada_1, entrada_2, val_soma, val_mul, val_sub, val_div, div_zero)

