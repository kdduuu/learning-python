# =====================================================
# PROGRAMA: CONCATENADOR DE PALAVRAS
# =====================================================


# -----------------------------------------------------
# Criando uma string vazia
# -----------------------------------------------------

# essa variável vai guardar todas as palavras digitadas
frase = ""


# -----------------------------------------------------
# Loop infinito
# -----------------------------------------------------

# o programa continuará rodando até o usuário digitar "/exit"
while True:

    # pede uma palavra ao usuário
    palavra = input("Digite uma palavra (/exit para sair): ")


    # -------------------------------------------------
    # Verifica se o usuário quer encerrar o programa
    # -------------------------------------------------

    # se a palavra digitada for "/exit"
    if palavra == "/exit":

        # encerra o loop
        break


    # -------------------------------------------------
    # Concatena a palavra na frase
    # -------------------------------------------------

    # adiciona:
    # palavra digitada + espaço
    frase = frase + palavra + " "


# -----------------------------------------------------
# Exibindo o resultado final
# -----------------------------------------------------

print()

# mostra todas as palavras concatenadas
print("Resultado da concatenação:")
print(frase)