'''
'' EXERCICIO DE ESTUDO DAS ESTRUTURAS DE LOOP COM LIMITE DE REPETIÇÃO
'' 
'' 
''' 
import os
from time import sleep
#########################################################################
####   Define funções para o cabeçalho, rodapé, limpar tela e linha  ####
def cabecalho():
    linha()
    texto_centralizado("USO DE ESTRUTURA DE REPETIÇÃO")
    linha()
#######
def rodape():
    linha()
    texto_centralizado("FIM DO PROGRAMA")
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
###               Funções de execução dos exercícios                  ###
def uso_range():
    limpar_tela()
    linha()
    texto_centralizado("Exercicio 1 - Avisos RH!")
    linha()
    for x in range(10, 0, -1):
        print(f"O treinamento começara em {x} minutos!")
        sleep(1)
    print("\nO treinamento começou!")
    input("\nPressione enter para ir para a tela inicial...")
    linha()
#######
def lista_valores():
    limpar_tela()
    linha()
    texto_centralizado("Exercicio 2 - LISTA DE VALORES")
    linha()
    lista_valores = [2000,5000,1000,8000,3000]

    for x in lista_valores:
        if (x < 4000):
            comicao = x * 0.05
        else:
            comicao = x * 0.1
        print (f"Valor de venda: R${x} -> Comição: R${comicao}")
    
    input("\nPressione enter para ir para a tela inicial...")
    linha()
#######
def verifica_estoque():
    limpar_tela()
    linha()
    texto_centralizado("Exercicio 3 - VERIFICA ESTOQUE")
    linha()
    estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]
    estoque_quantidades = [5, 12, 2, 8, 15]
    estoque_minimo = 8

    for i in range(len(estoque_produtos)):
        if estoque_quantidades[i] < estoque_minimo:
            print(f"Produto: {estoque_produtos[i]} esta com estoque baixo! Quantidade: {estoque_quantidades[i]}")

    linha()
    input("\nPressione enter para ir para a tela inicial...")
####### EM CONSTRUCAO
def custo_mensal():
    metas = {"jan": 1000, "fev": 1200, "mar": 1100} 
    gastos = {"jan": 900, "fev": 1350, "mar": 1100}
    print(f"{metas['jan']}")
    sleep(2)


##########################################################################################
def menu():
    while True:
        limpar_tela()
        cabecalho()
        print("1 - range")
        print("2 - Lista de Valores:")
        print("3 - Estoque produtos:")

        print("0 - Finalizar o programa")
        linha()

        escolha = int(input("Escolha uma opção:"))
        match escolha:
            case 0:
                print("\nFinalizando o programa...")
                break
            case 1:
                uso_range()
            case 2:
                lista_valores()
            case 3:
                verifica_estoque()
            case 4:
                custo_mensal()

# Executa o programa
if __name__ == "__main__":
    menu()