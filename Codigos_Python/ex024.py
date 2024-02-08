#Crie um programa que leia o nome de uma cidade se ela começa ou não com o nome de "SANTO".
cidade = str(input('Em que cidade você nasceu?')).strip()
print(cidade[:5].upper() == 'SANTO')

