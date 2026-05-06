palavra = input("Digite uma palavra: ").strip().lower()

# print(palavra[-1])

if palavra: #verifica se não está vazia
    if palavra[0].lower() in "aeiou":
        print("A palavra começa começa com vogal.")
    else:
        print("A palavra começa com consoante.")
else:
    print("Nenhuma palavra foi digitada.")

qnt_vogais = 0

for i in palavra:
    if i in "aeiou":
        qnt_vogais += 1

print(qnt_vogais)