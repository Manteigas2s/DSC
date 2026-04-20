idade = int(input("Digite sua idade:"))
verif = idade >= 18

print(f"Acesso ao sistema:{verif}")

nome = input("Digite o nome do produto:")
preco = float(input("Digite o preço do produto:"))
quant_prod = int(input("Digite a quantidade do produto:"))

valor = preco * quant_prod
meta = valor >= 100

print(f"""Valor total é: R$ {valor:.2f}
Meta de venda: {meta}
""")

idade = int(input("Digite a idade do visitante:"))
peso = float(input("Digite o peso do visitante:"))

veri1 = idade >= 13
veri2 = peso >= 50

pode_descer = veri1 and veri2

print(f"""
      
    Checagem de idade:{veri1}
    Checagem do peso:{veri2}

    Autorizado:{pode_descer}


""")