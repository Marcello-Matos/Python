# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogadpor vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
contador = 0
result = 0

while True:
    numeroEscolhido = random.randint(0, 10)
    sorte = int(input('Escolha um número entre 0 e 10: '))
    contador += 1

    if sorte == numeroEscolhido:
        print('Eba, que felicidade, você acertou!')
        result += contador
        break
    else:
        print("Que pena, você errou, tente novamente")
print("\033[0;30;41m O número de tentativas foram {}.\033[m".format(result))



