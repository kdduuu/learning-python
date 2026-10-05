grupo1 = {"Carlos", "Josier", "Jandira", "Aline"}
grupo2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

print("Primeiro Grupo: ", grupo1)
print("Segundo Grupo: ", grupo2)

intersec = grupo1.intersection(grupo2)
simetrico = grupo1.symmetric_difference(grupo2)
uniao = grupo1.union(grupo2)

print("Pessoas em comum nos dois grupos: ", intersec)
print("Pessoas que estão apenas em um grupo: ", simetrico)
print("Todas as pessoas: ", uniao)
