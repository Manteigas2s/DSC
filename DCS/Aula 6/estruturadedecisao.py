idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Seu acesso está liberado")
    print("Você é maior de idade")

else:
    print("Seu acesso não está liberado")
    print("Você não é maior de idade")

print("Boa noite!")

pergunta = input("Qual o turno atual? (Manhã/Tarde/Noite/Madrugada): ")

if pergunta == "Manhã" or pergunta == "manhã":
    print("Bom Dia!")

elif pergunta == "Tarde" or pergunta == "tarde":
    print("Boa Tarde!")     

elif pergunta == "Noite" or pergunta == "noite":
    print("Boa Noite!")

elif pergunta == "Madrugada" or pergunta == "madrugada":
    print("Boa Madrugada!")

else:
    print("Digite um turno válido!")