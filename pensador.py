import random
print('Vou pensar em um número de 1 a 10, tente advinhar!')
num= random.randint(1, 10)
#print(num)
n= int(input('Qual é o seu palpite? '))
if num == int(n):
    print('Parabéns, vocé acertou!')
else:
    print('Que pena, vocé errou!')