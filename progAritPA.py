pt =int(input('Digite o primeiro termo: '))
r =int(input('Digite a razão: '))
n = int(input('Digite o número de posições: '))

for c in range(pt,pt+n*r,r): 
    print(c, end=' ')



p = int(input('\nQual posição você quer descobrir um número?  '))
an = pt + (p - 1) * r

print('O {} termo é: {}'. format(p, an))


