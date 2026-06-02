valores = int(input('Digite QUATRO VALORES:   ')), int(input('Digite QUATRO VALORES:   ')), int(input('Digite QUATRO VALORES:   ')), int(input('Digite QUATRO VALORES:   '))
pares = 0

if 3 in valores:
    print(f'O número 3 foi digitado na posição {(valores.index(3))+1}')
else: 
    print(f'o número 3 não foi digitado')
   
print(f'O número 9 apareceu {(valores.count(9))} vezes; Os números pares foram: ', end=' ')
if 3 in valores:
    print(f'O número 3 foi digitado na posição {(valores.index(3))+1}')

for n in valores:
    if n % 2 == 0:
        print(n, end=',')
        
