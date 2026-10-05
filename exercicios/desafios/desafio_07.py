nota = float(input("Digite a nota: "))

if nota >= 7.0:
    print("Aprovado(a)!")
if nota < 7.0 and nota >= 4.0:
    print("Direito a Exame!")
if nota < 4.0:
    print ("Reprovado!")