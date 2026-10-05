# pede para o usuário digitar números separados por espaço
entrada = input("Digite 3 números separados por espaço: ")
# input → recebe entrada do usuário (sempre como texto)


# transforma a entrada em lista de números
numeros = list(map(int, entrada.split()))
# entrada.split() → separa o texto em partes
# ex: "10 20 30" → ["10", "20", "30"]

# map(int, ...) → aplica a função int em cada item
# ex: ["10", "20", "30"] → 10, 20, 30

# list(...) → transforma o resultado em lista
# resultado final → [10, 20, 30]


# mostra a lista completa
print("Lista:", numeros)
# print → mostra algo na tela


# mostra quantos números foram digitados
print("Quantidade:", len(numeros))
# len → retorna o tamanho da lista


# mostra o maior número
print("Maior número:", max(numeros))
# max → retorna o maior valor


# mostra o menor número
print("Menor número:", min(numeros))
# min → retorna o menor valor


# soma todos os números
print("Soma:", sum(numeros))
# sum → soma todos os valores