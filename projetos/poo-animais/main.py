# ============================================
# CLASSE BASE (classe "pai")
# ============================================

# Aqui estamos criando uma classe chamada Animal
# Ela será o modelo/base para outros animais
class Animal:

    # __init__ é o método construtor
    # Ele executa automaticamente quando criamos um objeto
    #
    # self -> representa o próprio objeto criado
    # nome -> valor que será recebido para o nome
    # especie -> valor que será recebido para a espécie
    def __init__(self, nome, especie):

        # Salva o nome dentro do objeto
        # Ex:
        # dog.nome = "Bilu"
        self.nome = nome

        # Salva a espécie dentro do objeto
        # Ex:
        # dog.especie = "Cachorro(a)"
        self.especie = especie

    # Método da classe Animal
    # Esse método retorna uma frase sobre o animal
    def fala(self):

        # f-string -> permite colocar variáveis dentro do texto
        #
        # self.nome -> pega o nome do objeto
        # self.especie -> pega a espécie do objeto
        #
        # Exemplo de retorno:
        # "Bilu é um(a) Cachorro(a)"
        return f"{self.nome} é um(a) {self.especie}"



# ============================================
# CLASSE CACHORRO
# ============================================

# Cachorro HERDA da classe Animal
#
# Isso significa:
# - Cachorro reaproveita tudo de Animal
# - já possui nome
# - já possui especie
# - já possui o método fala()
class Cachorro(Animal):

    # Construtor da classe Cachorro
    #
    # nome -> nome do cachorro
    # raca -> raça do cachorro
    def __init__(self, nome, raca):

        # super() chama a classe pai (Animal)
        #
        # Aqui estamos executando o __init__ da classe Animal
        #
        # Isso cria:
        # self.nome
        # self.especie
        #
        # "Cachorro(a)" será automaticamente a espécie
        super().__init__(nome, "Cachorro(a)")

        # Cria um novo atributo chamado raca
        #
        # Ex:
        # dog.raca = "Caramelo"
        self.raca = raca

    # Estamos SOBRESCREVENDO o método fala()
    #
    # A classe Animal já tinha um fala()
    # Mas aqui criamos uma versão própria para Cachorro
    def fala(self):

        # super().fala()
        # chama o método fala() da classe Animal
        #
        # Isso retorna:
        # "Bilu é um(a) Cachorro(a)"
        #
        # Depois adicionamos:
        # " e late"
        #
        # Resultado final:
        # "Bilu é um(a) Cachorro(a) e late"
        return f"{super().fala()} e late"



# ============================================
# CLASSE GATO
# ============================================

# Gato também HERDA da classe Animal
class Gato(Animal):

    # Construtor da classe Gato
    #
    # nome -> nome do gato
    # cor -> cor do gato
    def __init__(self, nome, cor):

        # Chama o construtor da classe Animal
        #
        # Isso cria:
        # self.nome
        # self.especie
        #
        # "Gato(a)" será a espécie automaticamente
        super().__init__(nome, "Gato(a)")

        # Cria um atributo chamado cor
        #
        # Ex:
        # cat.cor = "Rajado"
        self.cor = cor

    # Sobrescrevendo o método fala()
    def fala(self):

        # super().fala()
        # retorna:
        # "Pipoca é um(a) Gato(a)"
        #
        # Depois adicionamos:
        # " e mia"
        #
        # Resultado:
        # "Pipoca é um(a) Gato(a) e mia"
        return f"{super().fala()} e mia"



# ============================================
# CRIANDO OBJETOS
# ============================================

# Criando um objeto da classe Cachorro
#
# "Bilu" -> vai para nome
# "Caramelo" -> vai para raca
dog = Cachorro("Bilu", "Caramelo")

# Criando um objeto da classe Gato
#
# "Pipoca" -> vai para nome
# "Rajado" -> vai para cor
cat = Gato("Pipoca", "Rajado")



# ============================================
# EXIBINDO DADOS DO CACHORRO
# ============================================

# print() vazio apenas pula linha
print()

# Mostra um título na tela
print("Atributos do Cachorro:")

# Acessa o atributo nome do objeto dog
#
# dog.nome -> "Bilu"
print(f"Nome: {dog.nome}")

# Acessa o atributo raca
#
# dog.raca -> "Caramelo"
print(f"Raça: {dog.raca}")

# Acessa o atributo especie
#
# dog.especie -> "Cachorro(a)"
print(f"Espécie: {dog.especie}")

# Pula linha
print()

# Executa o método fala()
#
# Resultado:
# "Bilu é um(a) Cachorro(a) e late"
print(dog.fala())



# ============================================
# SEPARADOR VISUAL
# ============================================

print()
print("--------------------------------------------")
print()



# ============================================
# EXIBINDO DADOS DO GATO
# ============================================

print("Atributos do Gato:")

# cat.nome -> "Pipoca"
print(f"Nome: {cat.nome}")

# cat.cor -> "Rajado"
print(f"Cor: {cat.cor}")

# cat.especie -> "Gato(a)"
print(f"Espécie: {cat.especie}")

print()

# Executa o método fala()
#
# Resultado:
# "Pipoca é um(a) Gato(a) e mia"
print(cat.fala())

# Apenas pulando linhas
print()
print()