print('Bem vindo ao CONVERSOR DE NÚMEROS!')
# Este programa converte números decimais para binário, octal e hexadecimal.
n = float(input('Digite um valor: '))
bc = input('Digite 1 para Binário, 2 para Octal, 3 para Hexadecimal: ')
if bc == '1':
    print('O valor do número {} em binário é: {}'.format(n, bin(int(n))))
elif bc == '2':
    print('O valor do número {} em octal é: {}'.format(n, oct(int(n))))
elif bc == '3':
    print('O valor do número {} em hexadecimal é: {}'.format(n, hex(int(n))))