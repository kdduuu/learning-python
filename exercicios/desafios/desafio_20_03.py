# ==================================================
# MUTABILIDADE E IMUTABILIDADE EM PYTHON
# ==================================================

'''
Em Python, toda variável aponta para um objeto
guardado na memória.

A função id() mostra o identificador desse objeto,
como se fosse o "endereço" dele na memória.
'''

# ==================================================
# IMUTABILIDADE
# ==================================================

'''
Objetos imutáveis NÃO podem ser alterados.

Quando tentamos "mudar" o valor,
o Python cria um NOVO objeto na memória.
Por isso o ID muda.

Tipos imutáveis mais comuns:
- int
- float
- str
- bool
- tuple
'''

variavel_numerica = 5

print("Variável numérica antes da alteração")
print("Conteúdo:", variavel_numerica)
print("ID:", id(variavel_numerica))

'''
Aqui a variável aponta para o objeto 5
'''

variavel_numerica = 10

'''
O Python NÃO alterou o número 5.

Ele criou um NOVO objeto com valor 10
e fez a variável apontar para esse novo objeto.

Por isso o ID muda.
'''

print("Variável numérica depois da alteração")
print("Conteúdo:", variavel_numerica)
print("ID:", id(variavel_numerica))


# ==================================================
# MUTABILIDADE
# ==================================================

'''
Objetos mutáveis podem ser alterados
sem criar um novo objeto.

O próprio objeto é modificado.
Por isso o ID continua igual.

Tipos mutáveis mais comuns:
- list
- dict
- set
'''

lista_mutavel = [10, 20, 30]

print("Lista antes das alterações")
print("Conteúdo:", lista_mutavel)
print("ID:", id(lista_mutavel))

'''
A lista foi criada na memória
e possui um ID próprio.
'''

lista_mutavel.append(40)

'''
append() adiciona um valor na MESMA lista.
Nenhuma nova lista foi criada.
'''

lista_mutavel[0] = 0

'''
Aqui alteramos o primeiro elemento da lista.
A lista continua sendo a mesma.
'''

print("Lista depois das alterações")
print("Conteúdo:", lista_mutavel)
print("ID:", id(lista_mutavel))


# ==================================================
# RESUMO
# ==================================================

'''
IMUTÁVEL:
- Não pode ser alterado
- O Python cria outro objeto
- O ID muda

MUTÁVEL:
- Pode ser alterado
- O mesmo objeto é modificado
- O ID permanece igual
'''