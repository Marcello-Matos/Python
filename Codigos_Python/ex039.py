#Faça um programa que leia o ano de um nascimento de um jovem e informe de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo de alistamento.
#Seu programa tam´bem deverá mostrar o campo que falta ou que passou o prazo.
from datetime import date
atual = date.today().year
def perguntar_sexo():
    nasc = int(input("Informe seu ano de nascimento: "))
    sexo = input('''Informe seu sexo:
[ 1 ] Masculino
[ 2 ] Feminino
Sexo: ''')
    return nasc, sexo
nasc, sexo_usuario = perguntar_sexo()
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
if sexo_usuario == '2':
    print("Pessoas do sexo feminino não são obrigadas ao serviço militar.")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print("Seu alistamento será daqui {} anos.".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {}.".format(ano))
else:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos.".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}.".format(ano))




