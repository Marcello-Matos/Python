#escreva um program que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
#foi multado. A multa vai custar R$:7.00 por cada km acima do limite.
import random
velocidade = float(input('Digite a velocidade do carro em Km/h:'))
veloAcima = 80
multa = 7.00
if velocidade > veloAcima :
    calculo = velocidade - veloAcima
    calculo1 = calculo * multa
    print('Você excedeu o limite de velocidade em {} Km/h'.format(calculo))
    print('Você ultrapassou o limite e será multado no valor de R$:{:.2f}'.format(calculo1))
else:
    print('Parabéns, você está dentro do limite de velociade')
