import math
import os

#math

x = 16
raiz_quad = math.sqrt(x)

print ("Raiz quadrada de", x, "é igual a", raiz_quad)

angulo = 45
seno = math.sin(angulo)
print ("o seno de", angulo, "é igual a", seno)

#os

diretorio = os.getcwd()
print ("O diretório corrente é", diretorio)

#função nativa
lista = [10, 20, 30]
tam = len(lista)
print ("A lista", lista, "tem", tam, "elementos")

soma = sum(lista)
print("A lista", lista, "tem um somátorio igual a", soma)

#os.system("cls")