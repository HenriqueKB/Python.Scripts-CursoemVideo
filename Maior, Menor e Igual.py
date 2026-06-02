print('Veja agora se um número é maior, menor ou igual a outro')
n1= float(input('Digite o primeiro número:'))
n2= float(input('Digite o segundo número:'))
if n1>n2:
    print('O número {} é maior que o número {}'.format(n1,n2))
elif n2>n1:
        print('O número {} é maior que o número {}'.format(n2,n1))
elif n1==n2:
    print('Os números {} e {} são iguais'.format(n1,n2))