#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A"
#Em que posição ela parece a primeira vez e em que posição ela aparece a última vez.
nome = str(input('Digite o nome completo do usuário:')).strip().upper()
print('A letra "A" aparece {} vezes na frase'.format(nome.count('A')))
print('A primeira letra "A" aparece na posição {}'.format(nome.index('A') + 1))
print('A última letra "A" apareceu na posição {}'.format(nome.rfind('A') + 1))






