# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
feminino = "masculino"
while feminino == "masculino":
    sexo = str(input("Informe o sexo da pessoa [F/M]:")).upper()
    if sexo == "F":
        print("O sexo da pessoa é Feminino")
    elif sexo == "M":
        print("O sexo da pessoa é Masculino")
    else:
        print("Você digitou a palavra incorreta, tente novamente:")



