soma = 0
contador = 0
produto = 1

for i in range(1,1001):
    if i % 2 == 0:
        print(i)
        soma += 1
        contador += 1
        produto *= i

print(f"A soma é: {soma} ")
print(f"A quantidade de números pares é: {contador} ")
print(f"O produto dos números é: {produto} ")