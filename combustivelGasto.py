tempo = float(input('Qual foi o tempo da viagem em horas? '))
velocidade_media = float(input('Qual foi a velocidade média da viagem em km/h? '))
print(f'O tempo foi de: {tempo} horas')
print(f'A velocidade média foi de: {velocidade_media} km/l')
distacia_percorrida = tempo * velocidade_media
print(f'A distância percorrida em foi de: {distacia_percorrida} km')
litros_usados = distacia_percorrida / 12
print(f'A quantidade de litros utilizados nesta voajem foram de: {round(litros_usados,1)}')