# Crie um sistema escolar onde para calcular a média de um aluno devemos receber 4 notas válidas (entre 0 e 10). Ao final exiba o status de aprovação do aluno.

print("BEM-VINDO AO SISTEMA ESCOLAR")

notas_validas = 0
soma_notas = 0

while notas_validas < 4:
    nota = float(input(f"Digite uma nota entre 0 e 10: "))
    
    if nota < 0 and nota > 10:
         print("Nota Inválida!")
         print("DIgite novamente...")
         continue
    
    notas_validas += 1
    soma_notas += nota

    if notas_validas >= 4:
          break
        
media = soma_notas/notas_validas
print(f"Média: {media}")

if media >= 7 and media <= 10:
    print(f"Você foi Aprovado!")
elif media >= 4 and media <= 7:
    print(f"Você está de Recuperação!")
elif media >= 0 and media < 4:
    print(f"Você foi Reprovado!")
else:
    print("Média invalida!")

