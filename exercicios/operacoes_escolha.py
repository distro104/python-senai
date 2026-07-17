'''
EXERCICIO FEITO EM SALA DE AULA PARA TESTAR A INSTALACAO E USO DE PLUGINS NO PYTHON
'''
import os

os.system('cls')

def tela_resultado(entrada_1,entrada_2,texto,resultado):
    os.system('cls')
    print ("==========================================================")
    print ("            CALCULO DE VALORES C/ ESCOLHA")
    print ("==========================================================")
    print (f"    VALOR1: {entrada_1}")
    print (f"    VALOR2: {entrada_2}")
    print (f"    ESCOLHA: {texto}")
    print (f"    RESULTADO: {resultado}")
    print ("==========================================================")

def tela_escolha():
    os.system('cls')
    print ("==========================================================")
    print ("            CALCULO DE VALORES C/ ESCOLHA")
    print ("==========================================================")
    print ("1 - Soma")
    print ("2 - Subtração:")
    print ("3 - Multiplicação:")
    print ("4 - Divisão:")
    print ("==========================================================")

entrada_1 = False
entrada_2 = False
operacao = False
while True:
    if not entrada_1:
        tela_escolha()
        entrada_1 = float(input("Digite o Primeiro valor:"))
    elif not entrada_2:
        tela_escolha()
        entrada_2 = float(input("Digite o Segundo valor:"))
    elif not operacao:
        operacao = int(input("Qual operação devo fazer?(Digite o numero equivalente):"))
    else:
        tela_resultado()
        break


if (operacao == 1):
    texto = "Você escolheu soma!"
    resultado = entrada_1 + entrada_2
elif (operacao == 2):
    texto = "Você escolheu subtração!"
    resultado = entrada_1 - entrada_2
elif (operacao == 3):
    texto = "Você escolheu multiplicação!"
    resultado = entrada_1 * entrada_2
elif (operacao == 4):
    texto = "Você escolheu divisão!"
    if (entrada_2 <= 0):
        resultado = "DIVISÃO POR ZERO O CALCULO NÃO PODE SER EXECUTADO! :("
    else:
        resultado = round((entrada_1 / entrada_2),1)
else:
    texto = "Você não escolheu uma opção inexistente!"
    resultado = "RESULTADO NÃO PODE SER FEITO POIS NÃO FOI FEITO UMA ESCOLHA DE OPERAÇÃO VALIDA..."

tela_resultado(entrada_1,entrada_2,texto,resultado)