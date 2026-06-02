lista = []
cont = 0 
while True: 
        l = (int(input('Digite um valor: ')))
        lista.append(l)
        cont += 1
            
        opc = str(input('Quer continuar? [S/N]')).upper().strip()

        if opc == 'N':
            print('Os valores digitados em ordem reversa são: ')
            lista.sort(reverse=True) 
            print(f'{lista}')

            print(f'Foram digitados {cont} valores no total.')

            if 5 in lista:
             print('Ora, o que temos aqui! Um belo 5 na sua lista!')

            break
        
        

        
        