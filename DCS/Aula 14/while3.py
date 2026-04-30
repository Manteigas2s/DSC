# 3. Em uma competição de corrida um programa deve receber quantos metros cada competidor correu. Execute o programa até que seja inserido 0 na quantidade de metros percorridos. Ao final mostre qual foi o maior percurso registrado.
# Bônus: Colete também o nome de cada competidor e exiba o nome do competidor com o maior percurso

maior = 0
nome_maior_percurso =  ""

while True:
    nome = input("Digite o nome do competidor: ")
    metros = float(input("Digite quantos metros foram percorridos: "))

    if metros < 0:
        print("Digite um valor positivo para distância da corrida!")
        continue
    
    if metros == 0:
        print("Encerrando cadastro de percursos!")
        break
    

    if metros > maior:
        maior = metros
        nome_maior_percurso = nome



print(f"O maior percurso foi: {maior} metros ")
print(f"O maior corredor foi: {nome_maior_percurso} ")