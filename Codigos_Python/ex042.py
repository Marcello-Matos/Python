# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tripo de
# triângulo será formado:
# - Equilátero: todos os lados são iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
print("-="*25)
print("ANALISADOR DE TRIÂNGULOS". center(50))
print("-="*25)
r1 = float(input("Informe o primeiro segmento:"))
r2 = float(input("Informe o segundo segmento:"))
r3 = float(input("Informe o terceiro segmento:"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print("O segmento Equilátero: Tem todos os lados iguais")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Os segmentos Isósceles: Tem os dois lados iguais")
    else:
        print("Os segmentos Escaleno: Todos os lados são diferentes.")
else:
    print("Os segmentos não formam um triângulo.")
