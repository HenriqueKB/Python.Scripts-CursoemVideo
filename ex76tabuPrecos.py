listagem = (
    'Pão', 1.00, 
    'Leite', 3.50, 
    'Pão de Queijo', 1.50, 
    'Doce de Leite', 3.00, 
    'Misto Quente', 4.00,  
    'Geleia', 2.50, 
    'Torta', 5.00, 
    'Bolo de Cenoura', 10.00)

print('LISTAGEM DE PREÇOS MERCADO MASTER')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R${listagem[pos]:.>1}')