#Funções nátivas do Python 
 
''' 
print() → mostra algo na tela
ex: print("olá")
'''

''' 
input() → recebe entrada do usuário
ex: nome = input("seu nome: ")
'''

''' 
len() → retorna o tamanho de algo
ex: len([1, 2, 3]) → 3
'''

''' 
type() → mostra o tipo da variável
ex: type(10) → int
'''

''' 
int() → converte para número inteiro
ex: int("10") → 10
'''

''' 
float() → converte para número decimal
ex: float("10.5") → 10.5
'''

''' 
str() → converte para texto
ex: str(10) → "10"
'''

''' 
bool() → converte para verdadeiro ou falso
ex: bool(0) → False
'''

''' 
range() → gera sequência de números
ex: range(5) → 0 até 4
'''

''' 
sum() → soma valores
ex: sum([1, 2, 3]) → 6
'''

''' 
max() → maior valor
ex: max([1, 5, 3]) → 5
'''

''' 
min() → menor valor
ex: min([1, 5, 3]) → 1
'''

''' 
abs() → valor absoluto (sem sinal)
ex: abs(-10) → 10
'''

''' 
sorted() → ordena uma lista
ex: sorted([3,1,2]) → [1,2,3]
'''

''' 
enumerate() → retorna índice + valor
ex: enumerate(["a","b"]) → (0,"a"), (1,"b")
'''

''' 
zip() → junta listas
ex: zip([1,2],["a","b"]) → (1,"a"), (2,"b")
'''

''' 
map() → aplica função em vários itens
ex: map(lambda x: x*2, [1,2,3])
'''

''' 
filter() → filtra elementos
ex: filter(lambda x: x>2, [1,2,3])
'''

''' 
any() → retorna True se algum for verdadeiro
ex: any([False, True]) → True
'''

''' 
all() → retorna True se todos forem verdadeiros
ex: all([True, True]) → True
'''

''' 
open() → abre arquivos
ex: open("arquivo.txt")
'''

''' 
help() → mostra ajuda sobre algo
ex: help(print)
'''

''' 
dir() → mostra atributos de algo
ex: dir(str)
'''

''' 
id() → mostra identificador único do objeto
ex: id(x)
'''

''' 
isinstance() → verifica tipo
ex: isinstance(10, int) → True
'''

''' 
callable() → verifica se pode ser chamado como função
ex: callable(print) → True
'''

''' 
locals() → mostra variáveis locais
ex: locals()
'''

''' 
globals() → mostra variáveis globais
ex: globals()
'''

''' 
chr() → converte número em caractere
ex: chr(65) → "A"
'''

''' 
eval() → executa expressão como código
ex: eval("2+2") → 4
cuidado: pode ser perigoso
'''

''' 
exec() → executa código Python
ex: exec("print(10)")
cuidado: pode ser perigoso
'''