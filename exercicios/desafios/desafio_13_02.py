lv = []  
# cria uma lista vazia chamada "lv"
# ela será usada para guardar todos os números digitados

while True:  
    # cria um loop infinito
    # o programa ficará repetindo para sempre
    # até encontrar um "break"

    dado = int(input("Digite um número inteiro: "))  
    # pede para o usuário digitar um número
    # input() recebe como texto
    # int() transforma em número inteiro
    # o valor digitado é guardado na variável "dado"

    if dado == 0:  
        # verifica se o número digitado é igual a 0

        break  
        # encerra o loop imediatamente
        # o programa sai do while

    lv.append(dado)  
    # adiciona o número digitado dentro da lista
    # append() coloca o elemento no final da lista

# mostra uma mensagem antes de exibir os números
print("\nElementos digitados:")

for elem in lv:  
    # percorre todos os elementos da lista "lv"
    # a cada repetição:
    # "elem" recebe um valor da lista

    print(elem, end=" ")  
    # mostra o elemento na tela
    # end=" " faz todos aparecerem na mesma linha
    # separados por espaço

# resultados finais
print("\n\nQuantidade de elementos:", len(lv))  
# len() conta quantos elementos existem na lista

print("Menor número:", min(lv))  
# min() pega o menor valor da lista

print("Maior número:", max(lv))  
# max() pega o maior valor da lista