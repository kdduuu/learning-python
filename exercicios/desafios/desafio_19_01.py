def maior_numero(A, B):
    if A > B: 
        return A
    else:
        return B
    
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))    

res = maior_numero(numero1, numero2)

print("O maior número é: ", res)