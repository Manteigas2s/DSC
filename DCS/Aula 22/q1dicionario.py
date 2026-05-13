pacientes = []

while True:
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    genero = input("Digite o gênero do paciente: ")
    peso = float(input("Digite o peso do paciente: "))

    novo_paciente = {
        "Nome": nome,
        "Idade": idade,
        "genero": genero,
        "peso": peso
    }

    pacientes.append(novo_paciente)

    resposta = input("Deseja encerrar o programa: (S/N): ")
    if resposta == "S":
        print("Encerrando cadastro")
        break
print("\nLista de Pacientes\n")
contador = 1
qnt_acima30 = 0
qnt_abaixo30 = 0
nomes_acima30 = []
nomes_abaixo30 = []

for p in pacientes:
    print(f"{contador}. {p["Nome"]}")
    contador +=1
    
    if qnt_acima30[idade] > 30:
        qnt_acima30 += 1
        nomes_acima30.append(pacientes["Nome"])
    
    if qnt_abaixo30[idade] <= 30:
        qnt_abaixo30 += 1
        nomes_abaixo30.append(pacientes["Nome"])

print(f"""
Total Acima de 30: {qnt_acima30} {nomes_acima30}

Total Abaixo de 30: {qnt_abaixo30} {nomes_acima30}
""")