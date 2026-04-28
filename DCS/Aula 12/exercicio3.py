# 3. Faça um programa que recebe um palpite de um usuário e verifica se esse palpite é igual o número secreto(usar um número aleatório). Permita que o jogador tenha até 3 tentativas.
# Bônus: Faça com o que o jogo encerre assim que o jogador acertar o número secreto.
# Bônus: Faça com que o jogo imprima uma mensagem especial para quando o número de tentativas chegar ao final.
import random
numero_secret = random.randint(0,10)
tentativas = 3

for i in range(3):
    print(f"Você tem {tentativas} tentativas!")
    palpite = int(input("Digite seu palpite de 0 a 10: "))
    tentativas -= 1

    if palpite == numero_secret:
        print("Você acertou!")
        break
    else:
        print("Você errou!")
        if tentativas == 0:
            print(f"Você gastou todas as tentativas! Comece o jogo novamente para tentar outra vez.")

print("Fim de Jogo!")