dc = 0


while dc != 7:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite mais um número: '))
    calcs = int(input('Digite 1 para soma; 2 para subtração; 3 para multiplicação; 4 para divisão; 5 para potência; 6 para divisão inteira; 7 para resto de divisão; 8 para sair do programa; '))
    if calcs == 1:
        print('O resultado da soma é {}'.format(n1 + n2))
    elif calcs == 2:
        print('O resultado da subtração é {}'.format(n1 - n2))
    elif calcs == 3:
        print('O resultado da multiplicação é {}'.format(n1 * n2))
    elif calcs == 4:
        print('O resultado da divisão é {}'.format(n1 / n2))
    elif calcs == 5:
        print('O resultado da potência é {}'.format(n1 ** n2))
    elif calcs == 6:
        print('O resultado da divisão inteira é {}'.format(n1 // n2))
    elif calcs == 7:
        print('O resultado do resto da divisão é {}'.format(n1 % n2))


    dc = int(input('Você deseja continuar? Digite 8 caso queira sair e 1 para continuar.'))

