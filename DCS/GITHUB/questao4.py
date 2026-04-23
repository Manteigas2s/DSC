idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 17:
    print("Você é uma criança!")
elif idade >= 18 and idade <= 59:
    print("Você é um Adulto!")
elif idade >= 60:
    print("Você é um Sênior!")
else:
    print("Você é um Alienígena!")