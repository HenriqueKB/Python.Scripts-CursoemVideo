import statistics
lista1 = {}
lista4 = []
opc = 'S'
while opc == 'S':
    lista1['nome'] = str(input('Digite o nome da pessoa: '))
    

    lista1['sexo'] = str(input('Digite o sexo M/F: ')).upper()

    lista1['idade'] = int(input('Digite a idade: '))

    lista4.append(lista1.copy())
    media = statistics.mean([pessoa['idade'] for pessoa in lista4])

    opc = str(input('Quer continuar? [S/N]')).upper().strip()
    #if opc /= 'SN':
        #print('s')
    if opc == 'N':
        print(f'{(lista4)}')
        break

print('CONTAGEM DE PESSOAS:')
print(f'\n{len(lista4)} pessoas cadastradas')

print('MÉDIA DE IDADE:')
print(f'\n{media} é a média de idade')

print('MULHERES CADASTRADAS')
print(f'\n As mulheres cadastradas foram: ', end='')
for i, v in enumerate(lista4):
    if v['sexo'] in 'Ff':
        print(v['nome'], end=', ')

print('PESSOAS COM IDADE ACIMA DA MÉDIA:')
for i, v in enumerate(lista):
    if v['idade'] > (somaidade / len(lista)):
        for k, valor in v.items():
            print(f'  -{k} é {valor} ;', end=' ')
#brasil.append(estado.copy())