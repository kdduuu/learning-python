# ==================================
# CADASTRO DE PRODUTOS - CORINTHIANS
# ==================================

# lista que vai guardar os produtos
produtos = []


# =========================
# MENU PRINCIPAL
# =========================
while True:

    print("\n====== LOJA DO CORINTHIANS ======")

    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Remover produto")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")


    # =========================
    # CADASTRAR PRODUTO
    # =========================
    if opcao == "1":

        produto = {}

        produto["id"] = input("ID do produto: ")
        produto["nome"] = input("Nome do produto: ")
        produto["preco"] = float(input("Preço: "))
        produto["estoque"] = int(input("Quantidade em estoque: "))

        produtos.append(produto)

        print("Produto cadastrado com sucesso!")


    # =========================
    # LISTAR PRODUTOS
    # =========================
    elif opcao == "2":

        if len(produtos) == 0:
            print("Nenhum produto cadastrado!")

        else:

            print("\n=== PRODUTOS ===")

            for produto in produtos:

                print("\nID:", produto["id"])
                print("Nome:", produto["nome"])
                print("Preço: R$", produto["preco"])
                print("Estoque:", produto["estoque"])


    # =========================
    # BUSCAR PRODUTO
    # =========================
    elif opcao == "3":

        busca = input("Digite o nome do produto: ")

        encontrado = False

        for produto in produtos:

            if produto["nome"] == busca:

                print("\nPRODUTO ENCONTRADO")

                print("ID:", produto["id"])
                print("Nome:", produto["nome"])
                print("Preço: R$", produto["preco"])
                print("Estoque:", produto["estoque"])

                encontrado = True

        if encontrado == False:
            print("Produto não encontrado!")


    # =========================
    # REMOVER PRODUTO
    # =========================
    elif opcao == "4":

        remover = input("Digite o ID do produto: ")

        removido = False

        for produto in produtos:

            if produto["id"] == remover:

                produtos.remove(produto)

                print("Produto removido!")

                removido = True

        if removido == False:
            print("Produto não encontrado!")


    # =========================
    # SAIR
    # =========================
    elif opcao == "5":

        print("Encerrando sistema...")
        break


    # =========================
    # OPÇÃO INVÁLIDA
    # =========================
    else:
        print("Opção inválida!")