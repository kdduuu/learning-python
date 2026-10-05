contador = 0  
# cria a variável contador e começa com valor 0

for i in range(1, 1000):  
    # cria um laço de repetição que vai rodar várias vezes (até 1000)
    # aqui o "i" não é importante, ele só mantém o loop funcionando

    print("Contador:", contador)  
    # mostra na tela o valor atual do contador

    opcao = input("Digite 1 para incrementar ou 0 para sair: ")  
    # pede ao usuário uma opção e guarda na variável "opcao"

    if opcao == "0":
        print("Programa Encerrado!")
        break  
        # se o usuário digitar 0:
        # o "break" encerra o loop imediatamente (para o programa)

    if opcao != "1":
        continue  
        # se o usuário digitar qualquer coisa diferente de 1:
        # o "continue" faz o programa voltar pro início do loop
        # ou seja, não incrementa o contador

    contador += 1  
    # só chega aqui se o usuário digitou "1"
    # então soma +1 ao contador