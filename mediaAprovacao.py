m1 = float(input('Qual a primeira nota? '))
m2 = float(input('Qual a segunda nota? '))
m3 = float(input('Qual a terceira nota? '))
media = (m1 + m2 + m3) / 3
print(f'A sua media foi de: {round(media,1)}')
if media >= 0.0 and media <= 4.0:
    print('Você está reprovado')
elif media >= 4.1 and media <= 6.0:
    print('Você pegou exame')
    exame = float(input('Qual a nota no exame? '))
    if exame >= 6.0:
        print('Você passou')
    else:
        print('Você reprovou')
else:
    print('Você passou')
