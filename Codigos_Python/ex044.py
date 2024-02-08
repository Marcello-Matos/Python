# Elabore um programa que calcule o valor a ser pago por um produto. Considerando o seu
# preço normal e condição de pagamento:
# - Á vista dinheiro/Cheque: 10% desconto
# - Á vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros
print("{:=^40}".format(" Magestic x Coded "))
produto = float(input("Informe o valor do produto R$: "))
parcela = int(input("Informe o número de parcelas: "))
if parcela == 1:
    desc1 = produto * 10 / 100
    valor_com_desconto = produto - desc1
    print("O valor do produto é {:.2f} com o desconto de {:.2f}% à vista.".format(valor_com_desconto, 10))
elif parcela == 2:
    desc2 = produto * 0.05
    valor_com_desconto = produto - desc2
    print("O valor do produto é {:.2f} com o desconto de {}% à vista no cartão.".format(valor_com_desconto, 5))
elif parcela == 3:
    valor_parcela = (produto + produto * 20 / 100) / parcela
    valor_total = valor_parcela * parcela
    print("O valor do produto é {:.2f} com acréscimo de 20% parcelado em 3x no cartão.".format(valor_total))
    print("O valor de cada parcela é {:.2f}.".format(valor_parcela))
else:
    print("O sistema só aceita parcelamento em 1x, 2x ou 3x no cartão de crédito.")
