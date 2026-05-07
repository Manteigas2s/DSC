# 5. Verificação de estoque
# Um mercadinho tem a lista estoque = ["arroz", "feijão", "macarrão", "leite", "óleo"]. Peça ao usuário um produto com input() e informe se ele está ou não disponível no estoque. Depois, exiba o estoque em ordem alfabética usando sorted().

estoque = ["arroz", "feijão", "macarrão", "leite", "óleo"]
produto = input("Digite o nome do produto: ")


if produto in estoque:
    print("Tem disponivel no estoque!")
else:
    print("Não tem disponivel no estoque!")

print("\nEstoque em ordem alfabética: ")
print(sorted(estoque))
