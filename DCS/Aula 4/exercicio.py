nome = input("Digite o seu nome:")
data1 = int(input("Digite o ano do seu nascimento:"))
data2 = 2026
subtracao = data2 - data1

print(f"Olá, {nome}! Você tem {subtracao}.")
print("--------------------")

nome = input("Digite o nome do produto:")
preco = float(input("Digite o valor do produto:"))
quant = int(input("Digite a quantidade do produto:"))

multiplicacao = quant * preco

print(f"Valor total a pagar do produto: {multiplicacao:.2f}")
print("--------------------")

nome = input("Digite o seu nome:")
nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
nota3 = float(input("Digite sua terceira nota:"))
nota4 = float(input("Digite sua quarta nota:"))

media = (nota1 + nota2 + nota3) / 4

print(f"Resultado da suas Notas: {media}")
