# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria
# de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SENIOR
# Acima: MASTER
from datetime import date
atual = date.today().year
ano_nascimento = int(input("Informe o ano de nascimento:"))
idade = atual - ano_nascimento
if idade <= 9:
    print("O atleta tem {} anos".format(idade))
    print("Categoria: Mirim")
elif idade <= 14:
    print("O atleta tem {} anos".format(idade))
    print("Categoria: Infantil")
elif idade <= 19:
    print("O atleta tem {} anos".format(idade))
    print("Categoria: Júnior")
elif idade <= 20:
    print("O atleta tem {} anos".format(idade))
    print("Categoria: senior")
else:
    print("O atleta tem {} anos".format(idade))
    print("Categoria: Master")


