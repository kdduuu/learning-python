print("Primeiro metódo de execução:\n")
print("Nome: Kadu Almeida de Araújo")
print("Idade: 19 anos")
print(f"Salário: R${1621.00: .2f}")
print("Nacionalidade: Brasileiro")

print()

print("Segundo metódo de execução:\n")
print(f"Nome: Kadu Almeida de Araújo\nNacionalidade: Brasileiro \nIdade: {23: d} ")
print(f"Salário de: R${1.621: .3f}")

print()

print("Terceiro metódo de execução:\n")
nome = "Kadu Almeida de Araújo"
idade = 19
salario = 1621
nacionalidade = "Brasileiro"

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Nacionalidade: {nacionalidade}")

print ()

#Comentários: 
##\n → quebra de linha (pula para a próxima linha)
#f"..." → f-string (string formatada)
#Permite colocar valores dentro de chaves

# {1621.00: .2f}
# 1621.00 = valor numérico
# : = separa o valor da formatação
# .2f:
# .2 → duas casas decimais
# f → número decimal (float)
# Resultado: R$1621.00

# {23: d}
# 23 = número inteiro
# : = separa valor da formatação
# d = formato de número inteiro (decimal)
# (nesse caso é opcional, mas garante que é inteiro)

# {1.621: .3f}
# IMPORTANTE:
# 1.621 no Python significa: um ponto seis dois um (1.621)
# NÃO é mil seiscentos e vinte e um!

# .3f:
# .3 → três casas decimais
# f → número decimal

# TERCEIRO METÓDO - (Sem F)
#print("Nome:", nome)
#print("Idade:", idade)
#print("Salário: R$", salario)
#print("Nacionalidade:", nacionalidade)

# TERCEIRO METÓDO - (Sem F + concatenação)
#print("Nome: " + nome)
#print("Idade: " + str(idade))
#print("Salário: R$" + str(salario))
#print("Nacionalidade: " + nacionalidade)