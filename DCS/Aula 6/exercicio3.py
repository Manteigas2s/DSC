print (input("Digite o nome do alundo"))

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1+n2+n3+n4) / 4
situacao = "Não informado"
if media >= 7 and media <=10:
    print(f"Sua nota é {media}: Aprovado")
    situacao = "Aprovado"

elif media <7 and media >=4:
    print(f"Sua nota é {media}: Recuperação")
    situacao = "Recuperação"

elif media <4 and media >=0:
    print(f"Sua nota é {media}: Reprovado")
    situacao = "Reprovado"

else:
    print("Não constatado")

