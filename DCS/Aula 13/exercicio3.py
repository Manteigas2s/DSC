# 3. Crie um programa que recebe 5 números reais, exiba na tela o maior entre os números inseridos.

maior = None
menor = None

for i in range(5):
    num = float(input(f"Digite um número real: "))
    
    if num == None:
         maior = num
         # 3. Crie um programa que recebe 5 números reais, exiba na tela o maior entre os números inseridos.

    if num == None:
         menor = num

    if num < menor:
         menor = num

print(f"""
O número maior é: {maior}
O número menor é {menor}
""")