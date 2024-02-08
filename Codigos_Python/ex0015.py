#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
#ele foi alugado. Calcule o preço a pagar, sabendo ue o carro custa R$:60,00 por dia e R$:0,15 por km rodado:
carro = float(input('Quantos dias o carro foi alugado?'))
carro1 = float(input('Quantos quilometros foram rodado?'))
resultado = (carro * 60) + (carro1 * 0.15)
print('O valor total a pagar é: {:.2f}'.format(resultado))


