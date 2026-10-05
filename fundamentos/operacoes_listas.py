# OPERAÇÕES COM LISTAS EM PYTHON

'''
append(<elemento>)
→ adiciona um elemento no FINAL da lista

ex:
lista = [1, 2]
lista.append(3)

resultado:
[1, 2, 3]
'''

'''
extend(<iterável>)
→ adiciona vários elementos na lista

ex:
lista = [1, 2]
lista.extend([3, 4, 5])

resultado:
[1, 2, 3, 4, 5]
'''

'''
insert(<posição>, <elemento>)
→ adiciona um elemento em uma posição específica

ex:
lista = [1, 2, 3]
lista.insert(1, 10)

resultado:
[1, 10, 2, 3]
'''

'''
remove(<elemento>)
→ remove um elemento pelo VALOR

ex:
lista = [1, 2, 3]
lista.remove(2)

resultado:
[1, 3]
'''

'''
index(<elemento>)
→ mostra a posição de um elemento na lista

ex:
lista = [10, 20, 30]
print(lista.index(20))

resultado:
1
'''

'''
pop()
→ remove o ÚLTIMO elemento da lista

ex:
lista = [1, 2, 3]
lista.pop()

resultado:
[1, 2]
'''

'''
pop(<posição>)
→ remove um elemento de uma posição específica

ex:
lista = [10, 20, 30]
lista.pop(1)

resultado:
[10, 30]
'''

'''
count(<elemento>)
→ conta quantas vezes um elemento aparece na lista

ex:
lista = [1, 2, 2, 3]
print(lista.count(2))

resultado:
2
'''

'''
sort()
→ organiza a lista em ordem crescente

ex:
lista = [5, 1, 3]
lista.sort()

resultado:
[1, 3, 5]
'''

'''
reverse()
→ inverte a ordem dos elementos da lista

ex:
lista = [1, 2, 3]
lista.reverse()

resultado:
[3, 2, 1]
'''

'''
clear()
→ remove TODOS os elementos da lista

ex:
lista = [1, 2, 3]
lista.clear()

resultado:
[]
'''

'''
len()
→ mostra a quantidade de elementos da lista

ex:
lista = [10, 20, 30]
print(len(lista))

resultado:
3
'''

'''
sum()
→ soma todos os números da lista

ex:
lista = [1, 2, 3]
print(sum(lista))

resultado:
6
'''