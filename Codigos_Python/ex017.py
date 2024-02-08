#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo.
#Calcule e mostre o comprimento da hipotenusa:
cateto = float(input('Comprimento do cateto oposto:'))
adjacente = float(input('Comprimento do cateto adjacente:'))
hipotenusa = (cateto ** 2 + adjacente ** 2) ** (1/2)
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))
