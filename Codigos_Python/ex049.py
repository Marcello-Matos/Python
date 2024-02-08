# Refaça o desafio 009. mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
from time import sleep
print("-"*30)
numero = int(input("Informe a tabuada que deseja:"))
print("Bem Vindo a tabuada do {}:".format(numero))
for multiplicador in range(1, 11):
    sleep(1)
    resultado = numero * multiplicador
    print("{} x {} = {}".format(numero, multiplicador, resultado))
print("-"*30)
print("FIM DA EXECUÇÃO")

