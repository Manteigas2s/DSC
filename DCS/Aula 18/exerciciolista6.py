# 6. Controle de presença
# Uma turma tem 6 alunos. Use um for com enumerate() para percorrer a lista de nomes e perguntar ao usuário "presente" ou "ausente" para cada um. Ao final, exiba quantos alunos estiveram presentes e quantos faltaram.

alunos = ["pedro", "tarek", "iarley", "vagner", "mario"]

presentes = 0
ausentes = 0

for i in range(6):
    aluno = input("Digite presente ou ausente: ")
    