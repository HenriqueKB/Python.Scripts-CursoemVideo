import math
print('Bem vindo ao Calculador de Média Ponderada 2500!')
m1 = float(input('Digite sua média do primeiro bimestre: '))
m2 = float(input('Digite sua média do segundo bimestre: '))
m3 = float(input('Digite sua média do terceiro bimestre: '))
m4 = float(input('Digite sua média do quarto bimestre: '))
p1 = 1
p2 = 2
p3 = 4
p4 = 8
vf = (p1*m1 + p2*m2 + p3*m3 +
p4*m4) / (p1 + p2 + p3 + p4)


if vf < 60:
print("Você foi reprovado!")
    if vf > 50:
    print("Você chegou perto!")
    elif vf < 0:
    print("Nunca mais pegue num livro")

elif vf > 60:
print("VocÊ foi aprovado!")
    elif vf > 80:
    print("Você foi incrível!") 

print('Sua média final é: {:2} e você está '.format(vf))






