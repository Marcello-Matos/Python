#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo sem considerar o espaços.
nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome....')
print('Seu nome completo é: {}'.format(nome))
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúscula é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

