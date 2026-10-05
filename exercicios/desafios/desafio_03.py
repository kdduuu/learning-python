#nome = input("Digite seu nome: ")
#idade = int(input("Digite sua idade: "))
#altura = float(input("Digite sua altura: "))

#print ("O nome do usuário é:", nome)
#print ("A idade do usuario é:", idade)
#print ("A altura do usuário é:", altura)

id = int(input("Digite seu id: "))
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
nacionalidade = bool(input("Você nasceu no Brasil? "))

print("Os Dados do usuário são: "
      f"\n Nome: {nome}"
      f"\n Id: {id}"
      f"\n Salário: {salario}"
      f"\n Brasileiro: {nacionalidade}")

input(f"Os dados estão corretos? Sim/Não\n")

print("Dados registrados com sucesso!")