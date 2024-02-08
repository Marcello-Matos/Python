#Escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milimitros.
medida = float(input('Digite uma distância em metros:'))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
