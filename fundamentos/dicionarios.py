# Funções de Dicionários (dict)

'''
keys() → retorna todas as chaves do dicionário
ex:
produto = {"id": 1, "nome": "Mouse"}

print(produto.keys())

resultado:
dict_keys(['id', 'nome'])
'''

'''
values() → retorna todos os valores do dicionário
ex:
produto = {"id": 1, "nome": "Mouse"}

print(produto.values())

resultado:
dict_values([1, 'Mouse'])
'''

'''
items() → retorna chave e valor juntos
ex:
produto = {"id": 1, "nome": "Mouse"}

print(produto.items())

resultado:
dict_items([('id', 1), ('nome', 'Mouse')])
'''

'''
popitem() → remove o último item do dicionário
ex:
produto = {"id": 1, "nome": "Mouse"}

produto.popitem()

print(produto)

resultado:
{'id': 1}
'''

'''
update() → adiciona ou atualiza informações no dicionário
ex:
produto = {"id": 1}

produto.update({"nome": "Teclado"})

print(produto)

resultado:
{'id': 1, 'nome': 'Teclado'}
'''

'''
clear() → remove todos os itens do dicionário
ex:
produto = {"id": 1, "nome": "Mouse"}

produto.clear()

print(produto)

resultado:
{}
'''

'''
len(dict) → mostra a quantidade de itens do dicionário
ex:
produto = {"id": 1, "nome": "Mouse"}

print(len(produto))

resultado:
2
'''

'''
issubset() → verifica se um conjunto está dentro de outro
(essa função é usada em sets, não em dicts)
ex:
a = {"id", "nome"}
b = {"id", "nome", "preco"}

print(a.issubset(b))

resultado:
True
'''

'''
pop(chave) → remove uma chave específica
ex:
produto = {"id": 1, "nome": "Mouse"}

produto.pop("nome")

print(produto)

resultado:
{'id': 1}
'''

'''
fromkeys() → cria um dicionário usando chaves definidas
ex:
chaves = ["id", "nome", "preco"]

produto = dict.fromkeys(chaves)

print(produto)

resultado:
{'id': None, 'nome': None, 'preco': None}
'''

'''
setdefault() → retorna o valor da chave
se ela não existir, cria automaticamente
ex:
produto = {"id": 1}

produto.setdefault("nome", "Mouse")

print(produto)

resultado:
{'id': 1, 'nome': 'Mouse'}
'''