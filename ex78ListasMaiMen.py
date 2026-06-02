listanum = []
mai = 0 
men = 0
for c in range (0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c  == 0: #a partir do PRIMEIRO VALOR QUE EU DIGITO, ele JA é o MAIOR E MENOR.
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'{listanum}')

print(f'O MAIOR VALOR DIGITADO É: {mai} E SUA POSIÇÃO É: ', end = '')
print(f'O MENOR VALOR DIGITADO É: {men} E SUA POSIÇÃO É: ', end='')
for c,v in enumerate(listanum):
    if v == mai: 
        print(f'{c}-')
    if v == men:
        print(f'{c}-')
print()