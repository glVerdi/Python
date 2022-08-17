def leitura():
    tempo = float(input('Digite o tempo da viagem em horas: '))
    velocidade = float(input('Digite a velocidade média em km: '))
    return tempo, velocidade

def calcula_distancia(tempo, velocidade):
    return tempo * velocidade

def calcula_litros(distancia):
    return distancia / 12

def resultado(velocidade, tempo, distancia, litros):
    print('Velocideda: ', velocidade)
    print('Tempo: ', tempo)
    print('Distância: ', distancia)
    print('Litros: ', litros)

t, v = leitura()
d = calcula_distancia(t, v)
l = calcula_litros(d)
resultado(v, t, d, l)