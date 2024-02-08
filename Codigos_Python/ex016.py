#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
valor = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(valor, math.trunc(valor)))



