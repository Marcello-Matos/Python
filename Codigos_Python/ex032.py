#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Que ano você gostaria de analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 40 == 0 and ano % 100 != 0 or ano % 400 == 0: #O ano bissexto é de 4 em 4 anos
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))


