print('ANALISADOR DE TRIÂNGULOS DO MAGO HENRICÃO')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')

n1= float(input('Digite um número: '))
n2= float(input('Digite mais um número: '))
n3= float(input('Digite o último número: '))

#condições aninhadas, peercebe-se que pude criar if e elif deentro de um if
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Será possível ter um triângulo', end='')
    if n1 == n2 == n3:
        print(' equilátero.')
    elif n1 != n2 != n3 != n1:
        print(' escaleno.')
    else: 
        print(' isósceles.')

else: 
    print('Não será possível ter um triângulo.')
