# 2. Fila de atendimento
# Uma clínica tem uma fila com os nomes: ["Carlos", "Beatriz", "Fábio", "Juliana", "Rafael"]. Adicione "Tatiane" ao final da fila e remova "Fábio" porque ele desistiu. Exiba a fila atualizada e o total de pessoas.

nomes = ["Carlos", "Beatriz", "Fábio", "Juliana", "Rafael"]

nomes.append("Tatiane")
nomes.remove("Fábio")

for i in nomes:
    print(f"{i}")
    
print(len(nomes))
