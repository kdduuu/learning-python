# Palavras reservadas do Python

''' 
if → condição
ex: if x > 10:
'''

''' 
else → "senão"
ex: if... else...
'''

''' 
elif → "senão se" (else if)
ex: if x == 1: elif x == 2:
'''

''' 
for → loop de repetição
ex: for i in range(5):
'''

''' 
while → loop enquanto condição for verdadeira
ex: while x < 10:
'''

''' 
def → define uma função
ex: def minha_funcao():
'''

''' 
return → retorna valor de uma função
ex: return x
'''

''' 
print → (não é keyword, mas MUITO usado) mostra algo na tela
ex: print("olá")
'''

''' 
True → valor booleano verdadeiro
'''

''' 
False → valor booleano falso
'''

''' 
and → operador lógico "E" (tudo precisa ser verdadeiro)
ex: True and False → False
'''

''' 
or → operador lógico "OU"
ex: True or False → True
'''

''' 
not → negação lógica
ex: not True → False
'''

''' 
in → verifica se algo está dentro de algo
ex: if x in lista:
'''

''' 
import → importa bibliotecas
ex: import math
'''

''' 
from → importa algo específico de um módulo
ex: from math import sqrt
'''

''' 
as → usado para dar apelido (alias)
ex: import math as m
'''

''' 
break → interrompe um loop
ex: para um for ou while antes de terminar
'''

''' 
continue → pula para a próxima repetição do loop
ex: ignora o resto do código no loop atual
'''

''' 
pass → não faz nada (placeholder)
ex: usado quando precisa de um bloco vazio
'''

''' 
None → representa "nada" / valor vazio
muito usado como valor padrão em funções
'''

''' 
is → verifica se são o mesmo objeto (memória)
ex: x is y
diferente de == (que compara valor)
'''

''' 
lambda → função rápida (sem nome)
ex: lambda x: x + 1
'''

''' 
try → tenta executar algo (tratamento de erro)
ex: try: ...
'''

''' 
except → captura erros (exceções)
ex: try: ... except:
'''

''' 
finally → sempre executa (com ou sem erro)
ex: try... finally
'''

''' 
raise → lança um erro
ex: raise ValueError("erro")
'''

''' 
with → gerencia recursos automaticamente (arquivos, etc)
ex: with open("file.txt") as f:
'''

''' 
class → cria uma classe (modelo de objeto)
ex: class Pessoa:
'''

''' 
del → apaga uma variável ou item
ex: del x
'''

''' 
global → indica variável global
ex: global x
usado quando você quer modificar uma variável fora da função
'''

''' 
assert → verifica se algo é verdadeiro (usado para testes)
ex: assert x > 0
'''

''' 
yield → retorna valores aos poucos (geradores)
ex: usado em funções generator
parecido com return, mas não encerra a função
'''

''' 
async → define função assíncrona
ex: async def func():
usado para coisas que rodam "ao mesmo tempo" (ex: requisições)
'''

''' 
await → espera resultado de algo assíncrono
ex: await func()
'''

''' 
nonlocal → modifica variável de escopo externo (não global)
usado dentro de funções aninhadas
'''