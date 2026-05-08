# 6. Controle de presença
# Uma turma tem 6 alunos. Use um for com enumerate() para percorrer a lista de nomes e perguntar ao usuário "presente" ou "ausente" para cada um. Ao final, exiba quantos alunos estiveram presentes e quantos faltaram.

alunos = ["pedro", "tarek", "iarley", "vagner", "mario"]

presentes = 0
ausentes = 0

for i, aluno in enumerate(alunos, start=1):
    status = input(f"{i}. {aluno} está presente ou ausente: ").lower()
    
    if status == "presente":
        presentes += 1
    else:
        ausentes += 1

print("\n Resumo da presença: ")
print(f"Presentes: {presentes}")
print(f"Ausentes: {ausentes} ")