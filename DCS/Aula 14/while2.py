# 2. Crie um programa que pede números inteiros até que seja digitado -1. Quando o usuário digitar -1 exiba a soma de todos os números

numero = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro (-1 para sair): "))

    if numero == -1:
        break
    
    soma += numero

print(f"{soma}")