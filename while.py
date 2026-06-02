n = 1 
r = 'S'
par = impar = 0
while r == 'S':
    n = int(input('Digite Um Valor: '))
    r = str(input('Digite S Para Continuar E N Para Parar A Leitura: ')).upper()
    if n % 2 == 0:
        par += 1 
    else:
        impar += 1 
print('Você digitou {} números pares e {} impares!'. format(par, impar))
