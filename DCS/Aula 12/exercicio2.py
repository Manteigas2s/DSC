# 2. Faça um programa que repete 4 vezes a seguinte operação: Pede uma nota de um aluno e acrescenta a nova nota à soma das notas. Ao final das repetições exiba a média do aluno e se ele foi aprovado, reprovado ou está de recuperação.(Defina as notas para cada condição)
nota_ex = int(input("Digite a quantidade de notas que você deseja: ")) 
soma = 0
contador = 0
boletim = ""

for i in range(nota_ex):
    nota = float(input(f"Digite a nota {i+1}: "))
    
    if nota >= 0 and nota <= 10:
        soma += nota
        contador += 1
        boletim += f"Nota {contador}: {nota}\n"
    else:
        print("Nota invalida")
media = soma / contador

print(f"A Média do Aluno foi: {media}")
if media >= 7 and media <= 10:
    print(f"Você foi Aprovado!")
elif media >= 4 and media <= 7:
    print(f"Você está de Recuperação!")
elif media >= 0 and media < 4:
    print(f"Você foi Reprovado!")
else:
    print("Média invalida!")

print(f"""Seu boletim é : 
{boletim}""")