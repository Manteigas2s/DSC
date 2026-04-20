# 3. Crie um programa que pede um número inteiro e verifique se ele é par. Imprima na tela o resultado da verificação:

num = int(input("Digite um número inteiro: "))

verif_par = num % 2 == 0 and num != 0

print(f"O número {num} é par? {verif_par}")