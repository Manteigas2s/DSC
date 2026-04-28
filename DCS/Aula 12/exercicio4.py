# 4. Receba o nome, o preço e a quantidade de 5 produtos diferentes. Ao final exiba o valor total que o cliente deverá pagar.
# Bônus: Exiba uma nota fiscal com tudo que foi comprado e as informações da venda ao final.

valor_final = 0
nota_fiscal = ""

for i in range(5):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qnt_prod = int(input("Digite a quantidade de produto: "))
    valor_compra = preco*qnt_prod
    valor_final += valor_compra
    nota_fiscal += f"{nome} | R$ {preco:.2f} | {qnt_prod} - R$ {valor_compra:.2f}\n"

print("--------------------------------")
print(f" ------------ NOTA FISCAL ------------")
print("NOME | PREÇO (R$) | QUANTIDADE - TOTAL (R$)")
print(nota_fiscal)
print(f"Valor total da compra é: R${valor_final:.2f}")