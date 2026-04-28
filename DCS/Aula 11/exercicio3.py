soma = 0

for i in range(0,1001):
    if i % 2 == 0:
        soma += i
        print(i)
print(f"A soma de tudo é: {soma}")