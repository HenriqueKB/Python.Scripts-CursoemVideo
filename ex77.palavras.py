palavras = ('Duplopensar', 'Desbom', 'Pararcrime', 'Pensamentocrime', 'Grande', 'Chocolate', 'Jesus', 'Ambição', 'Vontade', 'Ego', 'Neopentecostal', 'Seita')
vogais = ('a', 'e', 'i', 'o', 'u', 'ã', 'é', 'á', 'à', 'í', 'ó', 'õ')
#for pos in range(0, len(palavras)):
    #print(f'\n{palavras}', end ='   ')

for cont in range(0, len(palavras)):
    print(f'\n\nA palavra {palavras[cont]}.')
    for letras in palavras[cont]:
        if letras.lower() in vogais: 
            print(f'\nPossui as vogais {letras}', end = '')
        
        