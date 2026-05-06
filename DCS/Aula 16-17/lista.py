# print("--------- LISTA DE FRUTAS ---------")
# frutas = ["Maçã", "Pêra", "Uva", "Abacate", "Abacaxi"] # Ordenada, Mutável

# print(len(frutas))

# print(frutas[-1])

# print(frutas[3])


# print("--------- LISTA DE ANIMAIS ---------")
# animais = ["Coelho", "Lobo", "Girafa", "Urubu", "Sapo"]

# Adiciona vários elementos dentro:
# animais += ["Enguia", "Peixe", "Cachorro"]

# Adiciona um animal em ultimo lugar: 
# animais.append("Coruja")

# Inserir algum animal local inicial: 
# animais.insert(0, "Gato")

# Remove o ultimo animal: 
# animais.pop()

# Remove animal especifico: 
# animais.remove("Urubu")

# Substitui animal especifico: 
# animais[3] = "Galinha"

# print(f"\n{animais}\n")

# print("--------- LISTA DE PESSOAS ---------")
# Nome, Idade, Altura, Conta Paga
# pessoa = ["Michael", 35, 1.75, True]

# print(f"""
# Nome: {pessoa[0]}
# Idade: {pessoa[1]} anos 
# Altura: {pessoa[2]} metros
# Conta Paga: {pessoa[3]}
# """)

print("--------- LISTA DE NUMEROS ---------")

numeros = [10, 50, 30, 25, 13]

soma = sum(numeros)
maior_numero = max(numeros)
menor_numero = min(numeros)
media = sum(numeros)/len(numeros)

# Método manual
# soma = 0 
# maior_numero = float("-inf")
# menor_numero = float("inf")

# for num in numeros:
#     soma += num
#     if num > maior_numero:
#         maior_numero = num

print(soma)
print(maior_numero)