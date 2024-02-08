#Crie um programa queleia um número inteiro e mostre na tela se ela é par ou impar.
num = float(input('Digite um número para sabermos se é par ou impar:'))
if num % 2 == 0 :
    print('O número digitado é {:.0f} par.'.format(num))
else:
    print('O número digitado é {:.0f} impar.'.format(num))
