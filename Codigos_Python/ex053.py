#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input("Digite uma frase:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("A frase digitada não é um palíndromo")
else:
    print("A frase digitada não é um plíndromo!")






