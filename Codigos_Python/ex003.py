#digite um programa que leia dois números e me mostre a soma entre eles.
valor = float(input('Digite um valor:'))
valor1 = float(input('Digite outro valor:'))
resp = valor + valor1
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
print('A soma entre {} {:.0f} + \033[31m{:.0f} \nO resultado é: \033[33m{:.0f}  {}'.format(cores['azul'], valor, valor1, resp, cores['amarelo']))

