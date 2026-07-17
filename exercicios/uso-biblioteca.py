'''
' Aula com foco no uso de bibliotecas como no exemplo PANDAS para manipulação
' de banco de dados.
' Instalação do PANDAS:
' Para a instalação da biblioteca utilize o comando:
' ======>  pip install pandas
'''

import  os
import pandas as pd

NOME_ARQUIVO = 'sistema_clientes.xlsx'

# 1. CONEXÃO E ESTRUTURA DO EXCEL
# Cria a planilha com cabeçalhos se o aquivo não existir
def inicializar_excel():
    # Verifica se o arquivo ja existe no computador
    if not os.path.exists(NOME_ARQUIVO):
        # Passo 1: Define as colunas vazias
        colunas = ['ID','Nome','E-mail','Telefone']
        df = pd.DataFrame(columns=colunas)
        # Cria uma estrutura dentro do arquvo vazia mas com os nomes da coluna acima

        # Passo 2: Salva o arquivo no formato .xlsx (excel)
        df.to_excel(NOME_ARQUIVO, index=False)

# 2. ALGORITIMO: CADASTRAR CLIENTE
def cadastrar_cliente():
    print("\n--- Novo Cadastro ---")

    # Passo 1: Carrega a planilha existete para a memoria
    df = pd.read_excel(NOME_ARQUIVO)

    # Passo 2: Recebe os dados do novo cliente
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o e-mail do cliente:")
    telefone = input("Digite o telefone do cliente:")

    # Passo 3: Gera um ID incremental baseado na quantidade de linhas
    novo_id = len(df) + 1

    # Passo 4: Cria uma nova linha com os dados informados
    nova_linha = {
        'ID': novo_id,
        'Nome': nome,
        'E-mail': email,
        'Telefone': telefone
    }

    # Passo 5: Adiciona a nova linha do DataFrame e salva o arquivo
    #df = pd.concat([df, pd.DataFrame([nova_linha])]), ignome_index=True)
    df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)
    print(f"Cliente {nome} cadastrado e salvo no Excel com sucesso!")

# 3. ALGORITMO: LISTAR CLIENTES
def listar_clientes():
    print("\n--- Lista de Clientes (Excel) ---")

    # Passo 1: Lê o arquivo do Excel
    df = pd.read_excel(NOME_ARQUIVO)

    # Passo 2: Verifica se a planilha está vazia
    if df.empty:
        print("Nenhum cliente cadastrado.")
    else:
        # Passo 3: Percorre linha por linha para exibir formatado
        for linha in df.iterrows():
            print(f"ID: {int(linha['ID'])} | \
                    Nome: {linha['Nome']} | \
                    E-mail: {linha['E-mail']} | \
                    Telefone: {linha['Telefone']}")

# 4. ALGORITMO: MENU PRINCIPAL
def menu():
    inicializar_excel() # Garante a existencia do arquvo excel ante de iniciar

    while True:
        print("\n=========================================")
        print("SISTEMA DE CADASTRO (EXCEL)")
        print("\n=========================================")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Sair")

        opcao = input("Escolha uma opção(1-3): ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            print("Saindo do sistema. Dados guardados no Excel!")
            break
        else:
            print("Opção invalida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()