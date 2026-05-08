# 4. Fatiamento de ranking
# Uma competição registrou os tempos (em segundos) dos 8 participantes em ordem de chegada: [12.3, 13.1, 13.8, 14.0, 14.5, 15.2, 16.0, 17.4]. Usando slicing, exiba apenas o pódio (os 3 primeiros), os 3 últimos colocados e os participantes do meio (posições 3 a 5).

tempos = [12.3, 13.1, 13.8, 14.0, 14.5, 15.2, 16.0, 17.4, 18.0]

podio = tempos[0:3]
ultimos = tempos[-3:]
meio = tempos[2:5]

print("Pódio", podio)
print("3 últimos colocados:", ultimos)
print("Participantes do meio:", meio)