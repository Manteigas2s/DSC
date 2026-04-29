print("MENU DE ATENDIMENTO")
pedido = input("Digite uma das opções (Ver extrato) (Conversar com Atendente) (Cancelar Conta): ")

if pedido == "Ver Extrato":
    print("O extrato estará disponivel em seu e-mail!")
elif pedido == "Conversar com Atendentes":
    print("Um funcionário entrará em contato pelo telefone!")
elif pedido == "Cancelar Conta":
    print("Não aceitamos o cancelamento da sua conta :)")
else:
    print("Escolha uma opção válida!")