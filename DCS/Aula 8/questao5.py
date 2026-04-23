preco_u = float(input("Digite o preço do produto: "))
quant_p = int(input("Digite a quantidade de produto: "))
valor_total = preco_u * quant_p

if preco_u > 100 or quant_p >= 5:
    print(f"O valor total é R$ {valor_total}. Você tem que pagar R$ {valor_total}")
elif preco_u <= 100 and quant_p >= 3:
    print(f"O valor total é R$ {valor_total}. Você tem que pagar R$ {valor_total}")
else:
    print(f"O valor total é R$ {valor_total}.Você tem que pagar R$ {valor_total}")
