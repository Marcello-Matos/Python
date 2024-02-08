# Faça um programa que mostre na tela uma contagem regressiva
#para o estouro de fogos de artifício, indo de 10 ate´0 com uma pausa de 1 Segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(2)
print("SEJA BEM VINDO 2024.")

