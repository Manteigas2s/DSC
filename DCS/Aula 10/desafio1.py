#1. Crie um programa que recebe três números inteiros e imprima o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if  num1 >= num2 and num1 >= num3:
    print(f"O número maior é {num1}.")
elif num2 >= num1 and num2 >= num3:
    print(f"O número maior é {num2}.")
elif num3 >= num1 and num3 >= num2:
    print(f"O número maior é {num3}.")
else:
    print("Não se enquadra em nenhuma das opções.")