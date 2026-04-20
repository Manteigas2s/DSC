print("Existe um número secreto entre 0 a 20!")
num_secret = 13

palpite = int(input("Fale qualquer número de 0 a 20 e tente acertar:"))

if  palpite == num_secret:
    print(f"Você acertou o número! O número secreto era: {num_secret}") 
    exit()
else:
    print("Você errou!")

    if palpite > num_secret:
        print(f"Seu palpite foi maior que o número secreto. Seu palpite foi: {palpite}")
    
    else:
        print(f"Seu palpite foi menor que o número secreto. Seu palpite foi: {palpite}")

print("--------------------------------------------")

palpite = int(input("Fale qualquer número de 0 a 20 e tente acertar:"))

if  palpite == num_secret:
    print(f"Você acertou o número na segunda tentativa! O número secreto era: {num_secret}")
    exit()
else:
    print(f"Você errou sua segunda tentativa! Só resta uma")
    if palpite > num_secret:
        print(f"Seu palpite foi maior que o número secreto. Seu palpite foi: {palpite}")
    
    else:
        print(f"Seu palpite foi menor que o número secreto. Seu palpite foi: {palpite}")

print("--------------------------------------------")

palpite = int(input("Fale qualquer número de 0 a 20 e tente acertar:"))

if  palpite == num_secret:
    print(f"Você acertou o número na segunda tentativa! O número secreto era: {num_secret}")
    exit()
else:
    print(f"Você errou sua terceira tentativa! Seu palpite foi: {palpite}")
    print(f"Você errou todas as tentativas! O número secreto era: {num_secret}")


        
