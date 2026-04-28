# 1. Receba 10 números inteiros. Imprima na tela a soma dos números e quantos eram números pares.

soma = 0
contador = 0

for i in range(0,10):
    num = int(input("Digite um número: "))
    if i % 2 == 0:
        soma += num
        contador += 1

print(f"A soma dos números é: {soma}")
print(f"A quantidade de números pares é: {contador}")