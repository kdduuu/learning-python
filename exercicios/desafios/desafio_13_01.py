lv = []  
# cria uma lista vazia chamada "lv"
# ela vai guardar todos os números digitados pelo usuário

s = 0  
# cria uma variável chamada "s"
# ela começa valendo 0
# essa variável será usada para somar os números digitados

for i in range(5):  
    # cria um loop que vai repetir 5 vezes
    # o "i" é uma variável de controle do loop
    # nesse código ela não está sendo usada diretamente
    # o range(5) gera:
    # 0, 1, 2, 3, 4
    # ou seja, 5 repetições

    dado = int(input("Digite um número inteiro: "))  
    # pede para o usuário digitar um número
    # input() recebe o valor como TEXTO
    # int() converte o texto para número inteiro
    # o valor digitado é guardado na variável "dado"

    lv.append(dado)  
    # adiciona o número digitado dentro da lista "lv"
    # append() serve para colocar elementos no final da lista

    s += dado  
    # soma o valor digitado na variável "s"
    # isso é a mesma coisa que:
    # s = s + dado

média = s / 5  
# calcula a média dos números
# pega a soma total (s)
# e divide por 5
# porque foram digitados 5 números

for elem in lv:  
    # percorre todos os elementos da lista "lv"
    # a cada repetição:
    # "elem" recebe um valor da lista

    print(elem, end=" ")  
    # mostra o elemento na tela
    # end=" " faz os números aparecerem na mesma linha
    # separados por espaço
    # sem isso, cada número apareceria em uma linha diferente

print(f"\nMédia dos elementos: {média}")  
# mostra a média final
# o "f" permite colocar variáveis dentro da string usando {}
# \n serve para pular uma linha antes da mensagem