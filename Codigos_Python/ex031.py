#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
#cobrando R$:0.50 por Km para viagens de até 200km é R$:0.45 para viagens mais longas.
distancia = float(input("Digite a distância da viagem em km: "))
print('Você está prestes a começar uma viagem de {:.0f}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O preço da passagem é R$:{:.2f}'.format(preco))

