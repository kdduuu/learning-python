nome_arquivo = input("Digite o nome do arquivo para armazenenar as palavras: ")

with open(nome_arquivo, 'w') as arquivo:
    while True: 
        palavra = input("Digite uma palavra (ou /exit para encerrar):")

        if palavra == "/exit":
            break

        arquivo.write(f"{palavra}\n")

print("Palavras armazenadas com sucesso... \n")

with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
