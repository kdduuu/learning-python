# OPERAÇÕES COM STRINGS EM PYTHON


'''
upper()
→ transforma todos os caracteres em MAIÚSCULOS

ex:
texto = "python"

resultado:
"PYTHON"
'''


'''
lower()
→ transforma todos os caracteres em MINÚSCULOS

ex:
texto = "PYTHON"

resultado:
"python"
'''


'''
strip()
→ remove espaços do COMEÇO e do FINAL da string

ex:
texto = "   olá   "

resultado:
"olá"
'''


'''
lstrip()
→ remove espaços apenas da ESQUERDA (início)

ex:
texto = "   olá"

resultado:
"olá"
'''


'''
rstrip()
→ remove espaços apenas da DIREITA (final)

ex:
texto = "olá   "

resultado:
"olá"
'''


'''
replace(<str1>, <str2>)
→ substitui uma string por outra

ex:
texto = "eu gosto de python"

resultado:
texto.replace("python", "java")

"eu gosto de java"
'''


'''
split(<separador>)
→ divide a string em partes e cria uma lista

ex:
texto = "maçã,banana,uva"

resultado:
texto.split(",")

['maçã', 'banana', 'uva']
'''


'''
join(<iterável>)
→ junta vários elementos em uma única string

ex:
lista = ["python", "java", "c++"]

resultado:
" - ".join(lista)

"python - java - c++"
'''


'''
startswith(<prefixo>)
→ verifica se a string COMEÇA com determinado texto

ex:
texto = "python"

resultado:
texto.startswith("py")

True
'''
 

'''
endswith(<sufixo>)
→ verifica se a string TERMINA com determinado texto

ex:
texto = "arquivo.txt"

resultado:
texto.endswith(".txt")

True
'''


'''
find(<substring>)
→ procura uma parte da string e retorna a posição

ex:
texto = "python"

resultado:
texto.find("th")

2
'''
 

'''
count(<substring>)
→ conta quantas vezes um trecho aparece

ex:
texto = "banana"

resultado:
texto.count("a")

3
'''


'''
isalpha()
→ verifica se existem apenas LETRAS

ex:
texto = "Python"

resultado:
texto.isalpha()

True
'''
 

'''
isdigit()
→ verifica se existem apenas NÚMEROS inteiros

ex:
texto = "12345"

resultado:
texto.isdigit()

True
'''
 

'''
isalnum()
→ verifica se existem apenas LETRAS e NÚMEROS

ex:
texto = "Python123"

resultado:
texto.isalnum()

True
'''
 

'''
isnumeric()
→ verifica se o conteúdo é numérico

ex:
texto = "500"

resultado:
texto.isnumeric()

True
'''