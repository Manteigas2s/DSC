# Crie uma calculadora onde a pessoa informa dois números e um operação (+,-,*,/). Ao terminar um cálculo exiba o resultado e pergunte se a pessoa deseja realizar outro cálculo. Caso a resposta seja sim, peça novamente os dois números e operação, caso a pessoa não deseje continuar encerre o programa.

print("CALCULADORA")
resultado = 0

while True:
    num1 = float(input("Digite o primeiro número: "))
    op = input("DIgite uma operação a seguir (+) (-) (*) (/); ")
    num2 = float(input("Digite o segundo número: "))

    if op == "+":
        resultado = num1 + num2

    elif op == "-":
        resultado = num1 - num2

    elif op == "*":
        resultado = num1 * num2

    elif op == "/":
        resultado = num1 / num2

        if num2 == 0:
            resultado = "TENTATIVA DE DIVISÂO POR 0"
        else:
            resultado = num1 / num2
    
    else:
        resultado = "OPERAÇÃO INVÁLIDA!"
    
    print(f"{num1} {op} {num2} = {resultado}")
    
    pergunta = input("Quer continuar? (S) ou (N): ")
    
    if pergunta == "N":
        break
    