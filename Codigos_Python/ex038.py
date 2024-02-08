#Escreva um programa que leia dois número inteiros e compare-os msotrando na tela uma mensagem:
#- O pirmeiro valor é Maior
#- O Segundo valor é maior
#- Não existe valor maior, os dois são iguais
num1 = int(input("Digite o Primeiro Número:"))
num2 = int(input("Digite o Segundo Número:"))
r1 = num1 > num2
r2 = num1 < num2
if r1 > r2:
    print("O Primeiro valor é Maior.")
elif r1 < r2:
    print("O Segundo Valor é Maior.")
else:
    print("Não existe valores maior, os dois são iguais.")


