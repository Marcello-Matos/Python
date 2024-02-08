#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
numeroEscolhido = random.randint(0, 5)
sorte = float(input('Escolha um número entre 0 a 5:'))
if sorte == numeroEscolhido :
    print('Eba, que felicidade, você acertou!'.format(numeroEscolhido))
else:
    print('Que pena, você errou, tente novamente!'.format(numeroEscolhido))


