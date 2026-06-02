n = int(input('Digite um número: '))
if n % 2 == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))
#a operação para verificar se é par ou ímpar é o resto da divisão por 2, 
# ou seja, se o resto da divisão por 2 for 0, ele é par, se for 1, ele é ímpar.