# Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. No final, mostre os 10 primeiros termos dessa progressão.
print("="*35)
print("10 TERMOS DE UMA PA!".center(35))
print("="*35)
primeiro_termo = 0
razao = 0
primeiro_termo = int(input("Qual é o primeiro termo da P.A:"))
razao = int(input("Qual é a razão do P.A:"))
decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo + razao, razao):
        print("{}".format(i), end=" → ")
print("ACABOU!")



