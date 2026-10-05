# FUNÇÕES DA CALCULADORA

def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Não existe divisão por zero!"
    else:
        return a / b


# MENU DE OPÇÕES

print("=== CALCULADORA ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha uma opção: ")

# RECEBE OS NÚMEROS

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# PROCESSAMENTO

if opcao == "1":
    res = soma(numero1, numero2)
    print("Resultado:", res)

elif opcao == "2":
    res = subtracao(numero1, numero2)
    print("Resultado:", res)

elif opcao == "3":
    res = multiplicacao(numero1, numero2)
    print("Resultado:", res)

elif opcao == "4":
    res = divisao(numero1, numero2)
    print("Resultado:", res)

else:
    print("Opção inválida!")