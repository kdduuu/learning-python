def calcula_quadrado(lista):
    for elem in lista:
        quad = elem ** 2
        print(f"O quadrado de {elem} é {quad}")

lista_de_inteiros = [1, 2, 3, 4, 5]

calcula_quadrado(lista_de_inteiros)