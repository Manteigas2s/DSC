# Crie um programa que pergunta se uma pessoa tem reserva para o restaurante. Verifique se a resposta foi especificamente "Sim" e imprima o resultado da verificação:

#Ex: "Entrada Permitida: {True/False}"
print("Bem-Vindo ao Restaurante")

reserva = input("Você tem uma reserva para o restaurante?")
verif = reserva == "Sim" or reserva == "sim"

print(f"Entrada concedida: {verif}")
