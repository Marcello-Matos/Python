#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto de 5% de desconto.
produto = float(input('Digite o valor do produto:'))
desconto = float(input('Digite o valor do desconto:'))
resultado = produto - (produto * desconto / 100)
print('O produto que custava R$:{:.2f}, na promoção com desconto de {:.0f}% vai custar R$:{:.2f}'.format(produto, desconto, resultado))

