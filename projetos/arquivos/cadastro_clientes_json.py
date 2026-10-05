# =========================================================
# IMPORTANDO A BIBLIOTECA JSON
# =========================================================

# A biblioteca json serve para transformar
# listas e dicionários do Python em arquivos .json
# e também fazer o contrário:
# pegar dados do arquivo e trazer para o Python

import json


# =========================================================
# NOME DO ARQUIVO
# =========================================================

# aqui o usuário digita o nome do arquivo
# ex:
# clientes.json

nome_arquivo = input("Digite o nome do arquivo: ")


# =========================================================
# LISTA PRINCIPAL
# =========================================================

# essa lista vai guardar TODOS os clientes

clientes = []


# =========================================================
# LOOP PRINCIPAL DO SISTEMA
# =========================================================

# while True cria um loop infinito
# o programa só para quando usar break

while True:

    # =====================================================
    # MENU
    # =====================================================

    print("\n--- MENU ---")

    print("1 - Cadastrar cliente")
    print("2 - Mostrar clientes")
    print("3 - Buscar cliente por CPF")
    print("4 - Alterar cliente")
    print("5 - Apagar cliente")
    print("6 - Sair")

    # usuário escolhe uma opção

    opcao = input("Escolha uma opção: ")


    # =====================================================
    # OPÇÃO 1 → CADASTRAR CLIENTE
    # =====================================================

    if opcao == "1":

        # cria um dicionário vazio
        # esse dicionário representa UM cliente

        cliente = {}

        # adiciona informações dentro do dicionário

        cliente["nome"] = input("Nome: ")
        cliente["cpf"] = input("CPF: ")
        cliente["telefone"] = input("Telefone: ")
        cliente["email"] = input("E-mail: ")
        cliente["endereco"] = input("Endereço: ")

        # adiciona o dicionário na lista de clientes

        clientes.append(cliente)

        # =================================================
        # SALVANDO NO ARQUIVO JSON
        # =================================================

        # with open() abre o arquivo

        # "w" significa WRITE (escrita)

        # se o arquivo não existir:
        # o Python cria automaticamente

        # se existir:
        # o conteúdo antigo é substituído

        with open(nome_arquivo, "w") as arquivo:

            # json.dump()
            # salva os dados no arquivo

            # clientes → lista que será salva

            # arquivo → arquivo aberto

            # indent=4
            # deixa o JSON organizado visualmente

            json.dump(clientes, arquivo, indent=4)

        print("\nCliente cadastrado com sucesso!")


    # =====================================================
    # OPÇÃO 2 → MOSTRAR CLIENTES
    # =====================================================

    elif opcao == "2":

        # abre o arquivo em modo leitura

        # "r" = READ

        with open(nome_arquivo, "r") as arquivo:

            # json.load()
            # lê o conteúdo do arquivo JSON
            # e transforma novamente em lista/dicionário Python

            clientes = json.load(arquivo)

        print("\n--- CLIENTES CADASTRADOS ---")

        # percorre todos os clientes da lista

        for cliente in clientes:

            # mostra os dados do cliente atual

            print(f"""
Nome: {cliente["nome"]}
CPF: {cliente["cpf"]}
Telefone: {cliente["telefone"]}
E-mail: {cliente["email"]}
Endereço: {cliente["endereco"]}
""")


    # =====================================================
    # OPÇÃO 3 → BUSCAR CLIENTE PELO CPF
    # =====================================================

    elif opcao == "3":

        # usuário digita o CPF que deseja buscar

        cpf_busca = input("Digite o CPF do cliente: ")

        # abre o arquivo para leitura

        with open(nome_arquivo, "r") as arquivo:

            # carrega os dados do JSON

            clientes = json.load(arquivo)

        # percorre todos os clientes

        for cliente in clientes:

            # verifica se o CPF atual
            # é igual ao CPF digitado

            if cliente["cpf"] == cpf_busca:

                print("\nCliente encontrado!")

                # mostra os dados encontrados

                print(f"""
Nome: {cliente["nome"]}
CPF: {cliente["cpf"]}
Telefone: {cliente["telefone"]}
E-mail: {cliente["email"]}
Endereço: {cliente["endereco"]}
""")


    # =====================================================
    # OPÇÃO 4 → ALTERAR CLIENTE
    # =====================================================

    elif opcao == "4":

        # usuário digita o CPF
        # do cliente que deseja alterar

        cpf_alterar = input("Digite o CPF do cliente: ")

        # abre o arquivo

        with open(nome_arquivo, "r") as arquivo:

            # carrega os dados

            clientes = json.load(arquivo)

        # percorre todos os clientes

        for cliente in clientes:

            # verifica se encontrou o CPF

            if cliente["cpf"] == cpf_alterar:

                print("\nDigite os novos dados:")

                # altera os dados do cliente

                cliente["nome"] = input("Novo nome: ")
                cliente["telefone"] = input("Novo telefone: ")
                cliente["email"] = input("Novo e-mail: ")
                cliente["endereco"] = input("Novo endereço: ")

        # =================================================
        # SALVA AS ALTERAÇÕES
        # =================================================

        with open(nome_arquivo, "w") as arquivo:

            # salva novamente a lista atualizada

            json.dump(clientes, arquivo, indent=4)

        print("\nCliente alterado com sucesso!")


    # =====================================================
    # OPÇÃO 5 → APAGAR CLIENTE
    # =====================================================

    elif opcao == "5":

        # usuário digita o CPF
        # do cliente que será apagado

        cpf_apagar = input("Digite o CPF do cliente: ")

        # abre o arquivo

        with open(nome_arquivo, "r") as arquivo:

            # carrega os clientes

            clientes = json.load(arquivo)

        # percorre todos os clientes

        for cliente in clientes:

            # verifica se encontrou o CPF

            if cliente["cpf"] == cpf_apagar:

                # remove o cliente da lista

                clientes.remove(cliente)

        # =================================================
        # SALVA A NOVA LISTA SEM O CLIENTE
        # =================================================

        with open(nome_arquivo, "w") as arquivo:

            json.dump(clientes, arquivo, indent=4)

        print("\nCliente apagado com sucesso!")


    # =====================================================
    # OPÇÃO 6 → SAIR DO PROGRAMA
    # =====================================================

    elif opcao == "6":

        print("\nPrograma encerrado...")

        # break encerra o while True

        break


    # =====================================================
    # CASO O USUÁRIO DIGITE UMA OPÇÃO INVÁLIDA
    # =====================================================

    else:

        print("\nOpção inválida!")