#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pinta-lo, sabendo que cada litro de tinta, pinta uma área de 2m².
alt = float(input('Digite a altura da parede:'))
larg = float(input('Digite a largura da parede:'))
total = (alt * larg) / 2
print('A altura da parede é: {:.0f} Metros e a largura é: {:.0f} Metros \nE o total de tinta que você vai usar é: {:.1f} litros de tinta.'.format(alt, larg, total))
