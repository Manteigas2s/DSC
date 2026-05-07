notas = []
alunos = []

while True:
    for i in range(2):
        aluno = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota: "))
        
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            alunos.append(aluno)
        else:
            print("Nota Invalída!")
        if len(notas) >= 8:
            break
        
    media = sum(notas)/len(notas)

    # ordem = 0
    # for n in notas:
    #     print(f"Nota {alunos[ordem]} - {n[ordem]:.1f}")
    #     ordem += 1

    # for aluno,nota in zip(alunos,notas):
    #     print(aluno,nota)

    for i,aluno in enumerate(alunos):
        print(f"{i+1}. {aluno} - {notas[i]}")