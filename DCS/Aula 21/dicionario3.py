# Crie um programa que guarda as pontuações do brasileirão. Para guardar essas pontuações use um dicionário onde a chave será o nome do time e o valor será a pontuação do time. Crie pelo menos 5 entradas.

brasileirao = {}

for i in range(2):
    Times = input("Digite o time: ")
    pontos = float(input("Digite a pontuação do time: "))
    brasileirao[Times] = pontos

print("\nTabela de classificação: \n")

for times, pontos in brasileirao.items():
    print(f"{Times}: {pontos} pontos")
    