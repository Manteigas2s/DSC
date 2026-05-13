# Faça um programa que pede as informações nome, espécie, peso e idade de um animal de atendimento veterinário. Salve essas informações em um dicionário e exiba a ficha do paciente.

animal = {}

animal["Nome"] = input("Digite o nome do animal: ")
animal["Espécie"] = input("Digite o nome da espécie: ")
animal["Peso"] = float(input("Digite o peso do animal: "))
animal["Idade"] = int(input("Digite a idade do animal: "))

print(f"""
Nome do animal: {animal['Nome']}
Espécie do animal: {animal['Espécie']}
Peso do animal: {animal['Peso']} kg
Idade do animal: {animal['Idade']} anos
""")