'''
'' Jogo da Velha - Versão em Python
'' Autor: Otavio J. Cruz
'' Data: 2024-06-10
'' Descrição: Este é um jogo da velha simples implementado em Python em que se simula um tabuleiro de 3x3 e permite que dois jogadores 
''            sendo um a maquina que faz escolhas aleatorias joguem alternadamente. O programa verifica as condições de vitória e empate,
''            exibindo o resultado ao final do jogo.
'''

def jogar():
    print ("Teste!!!!")

# Menu do jogo da velha
def menu():
    while True:
        print("==========================================================")
        print("                 JOGO DA VELHA - MENU")
        print("==========================================================")
        print("1 - Jogar")
        print("2 - Sair")
        print("==========================================================")
        print("                 |  X  |  X  |  X  |                            ")
        print("                 |  X  |  X  |  X  |                            ")
        print("                 |  X  |  X  |  X  |                            ")
        print("==========================================================")
        
        escolha = input("Escolha uma opção (1 ou 2): ")
        
        if escolha == '1':
            jogar()
        elif escolha == '2':
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    menu()