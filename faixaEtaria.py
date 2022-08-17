idade = int(input('Qual a sua idade? '))
if idade >= 0 and idade <= 12:
    print('Você é uma criança')
elif idade > 12 and idade <= 18:
    print('Você é um adolescente')
elif idade > 18:
    print('Você é um adulto')
else:
    print('Idade invélida')