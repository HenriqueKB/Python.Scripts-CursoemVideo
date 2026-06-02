lista = [] 
pares = []
impares = []
 
while True: 
        l = (int(input('Digite um valor: ')))
        lista.append(l)

        if l % 2 == 0: 
            pares.append(l)
        else:
            impares.append(l)
        
        opc = str(input('Quer continuar? [S/N]')).upper().strip()
        
        if opc == 'N':
          
            print(f'Os valores digitados são: {lista}')
            print(f'Os pares são: {pares}')
            print(f'Os impares são: {impares}')
            break
        
        

        
        