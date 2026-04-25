#3. Crie um programa que pede 10 números inteiros e imprima a soma deles.

soma = 0

for i in range(10):
    num = int(input("Digite um número: "))
    soma += num

print(f"A soma de todos os números é: {soma} ")