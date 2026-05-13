# Crie uma agenda telefonica onde o telefone da pessoa deve ser acessado pelo seu nome. Você deve usar um dicionário onde a chave será o nome e o valor será o telefone. Peça para que a pessoa escreva um nome e mostre na tela o telefone da pessoa escolhida. Faça pelo menos 10 contatos.

# Utilizando a agenda do problema anterior, realize as seguintes melhorias no programa:

# 1 - Peça para o usuário o nome e telefone de 5 novas pessoas e adicione na agenda.

# 2 - Utilize um loop while para permitir que a pessoa consulte os números da agenda. O usuário deverá escrever o nome de um dos contatos e o programa deve exibir o número na tela (caso exista, senão exibir mensagem de erro) e depois pedir o nome do próximo. Continue até que a pessoa escreva o nome "Sair".
# 3 - No começo de cada repetição, exiba a lista de contatos na tela.

agenda = {
    "Pedro": "85989261876",
    "Amanda": "85987654321",
    "Julia": "85123456789",
    "Marcus": "85321654987",
    "Geovana": "85654987321",
    "Hélio": "85213546879",
    "Gustavo": "85675819284",
    "Vinicius": "098765432112",
    "Felipe": "897654433210",
    "Matheus": "876554321901"
}

for i in range(5):
        nome = input("Digite o nome da pessoa: ")
        telefone = input("Digite o número de telefone: ")
        agenda[nome] = telefone

while True:
    print("\nLISTA DE CONTATOS\n")
    for n in agenda:
          print(f"{n}")

    nome = input("\nDigite o nome do contato que você deseja ver: ")
    
    if nome.upper() == "SAIR":
          print("Encerrando o programa!")
          break

    print(F"{nome}: {agenda.get(nome,"Nome não encontrado!")}")

    # if nome in agenda:
    #     print(agenda[nome])
    # else:
    #     print("Não encotrado na lista!")

    input("DIGITE ENTER PARA CONTINUAR!")