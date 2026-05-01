# Faça um menu de atendimento eletrônico que contenham as opções:

# 1. Falar com atendente
# 2. Finalizar contrato
# 3. Abrir nova conta
# 4. Visualizar segunda via da fatura
# 0. Sair

# Cada opção deve exibir uma mensagem relevante. Ao ver a mensagem, volte para o menu e peça uma nova opção do usuário. Se a pessoa escolher a opção Sair, encerre o programa. Caso a pessoa escreva uma opção inválida exiba uma mensagem de erro e volte para o menu.

while True:
    print("---------------- MENU DE ATENDIMENTO ----------------")
    print("""
    1. Falar com atendente
    2. Finalizar contrato
    3. Abrir nova conta
    4. Visualizar segunda via da fatura
    0. Sair 
    """)

    pergunta = input("Digite o número das opções acima: ")
    if pergunta == "1":
        print("Você será redirecionado para um atendente!")
    elif pergunta == "2":
        print("Finalizando contrato!")
    elif pergunta == "3":
        print("Abrindo nova conta!")
    elif pergunta == "4":
        print("Visualizando segunda via da fatura!")
    elif pergunta == "0":
        print("Saindo do Menu!")
        break
    else:
        print("Escolha uma opção válida!")
        
    input("APERTE ENTER PARA CONTINUAR")