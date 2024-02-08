# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso_maior = 0
peso_menor = 0
for peso in range(5, 0, -1):
    peso = float(input("Informe o quantos quilos tem as {}ª pessoas:".format(peso)))
    if peso > peso_maior:
       peso_maior = peso
    if peso_menor == 0 or peso < peso_menor:
       peso_menor = peso
if peso == peso_menor == peso_maior:
    print("Todos os pesos são iguais.")
else:
    print("A pessoa com maior peso é {:.1f}kg".format(peso_maior))
    print("A pessoa com menor peso é {:.1f}kg".format(peso_menor))







