import random
print('Vou pensar em um número de 1 a 10, tente advinhar!')
num= random.randint(1, 10)
tent = 0
n = int(input('Qual é o seu palpite? '))

while n != num:
    n = int(input('Tente novamente: '))
    tent += 1
if num == int(n):
    print('Parabéns, vocé acertou! Depois de {} tentativas!'.format(tent))
else:
    print('Que pena, você errou!')

conf = str(input('Você quer tentar advinhar de novo? DIGITE (S) para Sim ou (N) para não: '))


