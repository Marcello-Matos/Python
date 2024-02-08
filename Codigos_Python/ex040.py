#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado.
#Média entre 5.0 e 6.9: Recuperação
#Média 7.0 ou superior: Aprovado
nota1 = float(input("Informe a nota do primeiro aluno:"))
nota2 = float(input("Informe a segunda nota do aluno:"))
nota3 = float(input("Informe a terceira nota do aluno:"))
resultado = (nota1 + nota2 + nota3) / 3
if resultado < 5:
    print("Media abaixo de 5.0 aluno Reprovado:")
elif resultado == 5 and 6.9:
    print("A média entre 5.0 e 6.9 deixou você de recuperação:")
else:
    print("A sua média é {:.2f} você foi APROVADO:".format(resultado))
