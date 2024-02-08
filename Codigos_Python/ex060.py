# Criar um programa que rode os dias que vamos ter aula com a professora Ju.
import numpy as np
mes = str(input("Informe o mês do ano atual:"))
dias = int(input("Informe os dias da semana que vão ter aulas de 30 minutos:"))
fim_semana = int(input("Informe os finais de semana de 1 hora:"))
resultado1 = dias * 15
resultado2 = fim_semana * 30
resultado3 = resultado1 + resultado2
print("Os valores de 30 minutos são R$: {:.2f}\nValores de 1 hora são R$: {:.2f}\nDando um total de R$: {:.2f}".format(resultado1, resultado2, resultado3))
