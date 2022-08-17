nota = media = soma = 0
for _ in range(1, 6):
    nota = float(input('Digite a nota: '))
    soma += nota
print(f'A soma das notas foi de: {round(soma,1)}')
media = soma / 5
print(f'A média foi de: {round(media,1)}')