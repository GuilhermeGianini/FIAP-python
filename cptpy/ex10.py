notas = []

for aluno in range(3):
    notas_aluno = []

    for prova in range(4):
        nota = float(input("Digite a nota: "))
        notas_aluno.append(nota)

    notas.append(notas_aluno)

for aluno in range(3):
    media = sum(notas[aluno]) / 4
    print("Média do aluno", aluno + 1, ":", media)