#Faça um programa que leia trê números e mostre qual é o maior e qual é o menor.
import random
a = float(input('Digite um número:'))
b = float(input('Digite outro número:'))
c = float(input('Digite o último número:'))
maior = a
if b > a and b > c :
    maior = b
if c > a and c > b :
    maior = c
menor = a
if b < a and b < c :
    menor = b
if c < a and c < b :
    menor = c
    print('O número maior digitado foi: {:.0f} e o menor é: {:.0f}'.format(maior, menor))

