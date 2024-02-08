#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
real = float(input('Digite quanto você tem de dinheiro na carteira R$:'))
dollar = float(input('Digite o valor da cotação do dollar U$:'))
comprar = real / dollar
print('Com R$:{} você pode comprar U$:{:.2f} Dollares'.format(real, comprar))

