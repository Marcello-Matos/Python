#Escreva um programa que converta uma temperatura digitando em graus Celsius e vonverta para graus Fahrenheit.
temperatura = float(input('Digite a temperatura em graus Celsius:'))
temperatura1 = float(input('Digite a temperatura em graus Fahrenheit:'))
conversor = ((9 * temperatura) / 5) + 32
conversor1 = ((temperatura1 - 32) * 5) / 9
print('A temperatura em graus Celsius é {:.0f}°C convertido para Fahrenheit: {:.0f}°F'.format(temperatura, conversor))
print('A temperatura em Fahrenheit é: {:.0f}°F convertido para graus Celsius é: {:.0f}°C'.format(temperatura1, conversor1))
