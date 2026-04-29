numero = -1 
soma = 0
maior = float("-inf")
menor = float("inf")
contador_negativo = 0

while numero != 0:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    soma += numero

    if numero <0:
        contador_negativo += 1

    if numero > maior:
        maior = numero 

    if numero < menor:
        menor = numero


print(f"""
Soma: {soma}
Maior número é: {maior}
Menor número é: {menor}
A quantidade de número negativos é: {contador_negativo}

""")