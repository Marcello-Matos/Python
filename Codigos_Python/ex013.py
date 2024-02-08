#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario = float(input('Digite o valor do salário do funcionário:'))
aumento = float(input('Digite a porcetagem de aumento do funcionário:'))
resultado = salario + (salario * aumento / 100)
print('O Salário do funcionário é R$:{} com um aumento de {:.0f}% e vai passar a receber R$:{:.2f}'.format(salario, aumento, resultado))
