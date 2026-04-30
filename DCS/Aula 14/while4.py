qtd_func = 0

while True:
    nome_func = input("Digite o nome do funcionário: ")

    if nome_func == "SAIR":
        print("SAINDO DO CADASTRO DE FUNCIONÁRIOS")
        break

    qtd_func += 1

print(f"Funcionários Cadastrados: {qtd_func}")