# =====================================================
# PROGRAMA: MAIOR E MENOR ELEMENTO DE UMA MATRIZ 3x4
# =====================================================


# -----------------------------------------------------
# Definindo o tamanho da matriz
# -----------------------------------------------------

# quantidade de linhas da matriz
linhas = 3

# quantidade de colunas da matriz
colunas = 4


# -----------------------------------------------------
# Criando uma matriz vazia
# -----------------------------------------------------

# a matriz começará vazia
matriz = []


# -----------------------------------------------------
# Preenchendo a matriz com valores do usuário
# -----------------------------------------------------

print("Preencha a matriz 3x4:")


# percorre as linhas da matriz
for i in range(linhas):

    # cria uma lista vazia para armazenar os valores da linha
    linha = []

    # percorre as colunas da matriz
    for j in range(colunas):

        # pede um valor ao usuário
        valor = int(input(f"Digite o valor para a posição ({i},{j}): "))

        # adiciona o valor dentro da linha
        linha.append(valor)

    # adiciona a linha completa dentro da matriz
    matriz.append(linha)


# -----------------------------------------------------
# Inicializando maior e menor elemento
# -----------------------------------------------------

# pega o primeiro elemento da matriz
# ele será usado como valor inicial para comparação
maior = matriz[0][0]
menor = matriz[0][0]


# -----------------------------------------------------
# Variáveis para guardar as posições
# -----------------------------------------------------

# posição inicial do maior elemento
# começa em (0,0)
pos_maior = (0, 0)

# posição inicial do menor elemento
# começa em (0,0)
pos_menor = (0, 0)


# -----------------------------------------------------
# Procurando o maior e o menor elemento da matriz
# -----------------------------------------------------

# percorre as linhas da matriz
for i in range(linhas):

    # percorre as colunas da matriz
    for j in range(colunas):

        # verifica se o elemento atual é maior
        # que o maior encontrado até agora
        if matriz[i][j] > maior:

            # atualiza o maior valor
            maior = matriz[i][j]

            # guarda a posição do maior valor
            pos_maior = (i, j)

        # verifica se o elemento atual é menor
        # que o menor encontrado até agora
        if matriz[i][j] < menor:

            # atualiza o menor valor
            menor = matriz[i][j]

            # guarda a posição do menor valor
            pos_menor = (i, j)


# -----------------------------------------------------
# Exibindo a matriz completa
# -----------------------------------------------------

print("\nMatriz preenchida:")

# percorre cada linha da matriz
for linha in matriz:

    # mostra a linha inteira
    print(linha)


# -----------------------------------------------------
# Exibindo os resultados
# -----------------------------------------------------

print(f"\nO maior elemento é {maior} e está na posição {pos_maior}.")

print(f"O menor elemento é {menor} e está na posição {pos_menor}.")