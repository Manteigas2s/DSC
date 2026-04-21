#Revisão 2: Faça um programa de cadastro de funcionário onde são pedidos 5 informações de um funcionário (você escolhe as informações). Pelo menos uma informação deve ser número inteiro e outra informação deve ser número decimal(float). Ao final imprima a ficha do funcionário (use multi-linha)

func_nome = input("Digite o Nome:")
func_ano_nascimento = int(input("Digite o ano do nascimento:"))
func_altura = input("Digite a Altura:")
func_salario = float(input("Digite o Salário:"))
func_cpf = input("Digite somente o número do cpf::")
func_idade = 2026 - func_ano_nascimento

print(f"""
Ficha do funcionário:
      
    Nome: {func_nome}
    Idade: {func_idade}
    Altura: {func_altura}
    Salário: R$ {func_salario:.2f}
    CPF: {func_cpf}

""")





