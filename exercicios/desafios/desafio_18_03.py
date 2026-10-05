produtos = []

for _ in range(5):

    produto = {}

    produto["ID"] = input("Digite o ID do produto: ")
    produto["nome"] = input("Digite o nome do produto: ")
    produto["preço"] = float(input("Digite o preço do produto: "))

    produtos.append(produto)

    print()

    # mostra quantidade de produtos cadastrados
    print("Quantidade de produtos cadastrados:", len(produtos))

    print("Produtos cadastrados:")

    for produto in produtos:

        print()

        print("ID do produto:", produto["ID"])
        print("Nome do produto:", produto["nome"])
        print("Preço do produto:", produto["preço"])

        print()