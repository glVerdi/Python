alunos = {}
for _ in range (1, 4):
    nome = input('Digite um nome de aluno: ')
    nota = float(input('Digite a nota do aluno: '))
    alunos[nome] = nota
print(alunos)

soma = 0
for nota in alunos.values():
    soma += nota
print(f'Média: {round(soma / 3, 1)}')