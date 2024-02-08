# Faça um programa que calcule a soma entre todos os número impares que são multiplos de três
# e que se econtram no intevalo de 1 ate 500.
soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont = cont + 1
        soma = soma + num
print("A soma de todos os {} valores solicitados é {}".format(cont, soma))
