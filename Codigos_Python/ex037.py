#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolhe qual será a base de
#conversão:
# 1. Para Binário
# 2. Para Octal
# 3. Para Hexadecimal
#def decimal_para_binario(numero):
#    return bin(numero)[2:]
#def decimal_para_octal(numero):
#   return oct(numero)[2:]
#def decimal_para_hexadecimal(numero):
#   return hex(numero)[2:]
#
#def main():
#    numero = int(input('Digite um número decimal inteiro:'))
#    option = input('Escolha a base de conversão(1 para binário, 2 para octal, 3 para hexadecimal):')
#
#    if option == "1":
#        resultado = decimal_para_binario(numero)
#        print(f"O numero {numero} em binário é:{resultado}")
#    elif option == "2":
#        resultado = decimal_para_octal(numero)
#        print(f"O numero {numero} em Octal é:{resultado}")
#    elif option == "3":
#        resultado = decimal_para_hexadecimal(numero)
#        print(f"O numero {numero} em hexadecimal é:{resultado}")
#  else:
#       print("Opção Inválida!")

#main()

num = int(input("Digite um número inteiro:"))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int (input("Sua opção:"))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)))
else:
    print("Opção inválida. Tente Novamente.")