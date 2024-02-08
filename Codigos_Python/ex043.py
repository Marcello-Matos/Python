# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
# De acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso.
# - Entre 18.5 e 25: Peso Ideal
# - 25 até 30: SobrePeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
peso = float(input("Informe seu peso (KG):"))
altura = float(input("Informe a sua altura:"))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Seu IMC está {:.1f}. Você está abaixo do peso NORMAL.".format(imc))
elif 18.5 <= imc <= 25:
    print("Seu peso é {:.1f}. Você está no peso IDEAL.".format(imc))
elif 25 <= imc <= 30:
    print("Seu resultado é {:.1f}. Você está com SOBREPESO" " ATENÇÃO".format(imc))
elif 30 <= imc <= 40:
    print("Seu resultado é {:.1f}. Você está com OBESIDADE."" FIQUE EM ALERTA".format(imc))
else:
    print("Seu resultado é {:.1f}. Você está com obesidade mórbida."" PROCURE UM MÉDICO IMEDIATAMENTE".format(imc))


