lista = []
while True: 
        l = (int(input('Digite um valor: ')))
        if l not in lista:
            lista.append(l)
        else:
            print('VALOR DUPLICADO! Nem vou adicionar, seu tongo')
            
        opc = str(input('Quer continuar? [S/N]')).upper().strip()

        if opc == 'N':
            print('Vc digitou os valores: ')
            print(sorted(lista))
            break
        
        

        
        