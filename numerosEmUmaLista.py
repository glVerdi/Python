#import numpy as np
#np.array(lista).sum()
lista = []

for _ in range (1, 6):
    valor = int(input('Digite um número: '))
    lista.append(valor)
print(lista)

soma = 0
for i in range(len(lista)):
    soma += lista[i]
#print('Soma: ', soma)