tabela = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Santos', 'Corinthians', 'Vasco', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')
#print(tabela.index(5))
print('BEM VINDO AO RANK DO BRASILEIRÃO 2026')
while True: 
    opc  = int(input(
    'Você quer ver:'
    '[Digite 5] Os cinco primeiros colcoados?' 
    '[Digite 4] Os últimos quatro colocados?' 
    '[Digite 3] Quer ver a lista em ordem alfabética?' 
    '[Digite 2] Ou quer ver a posição de algum time de sua preferência? [DIGITE 0 para ENCERRAR]'))
    if opc == 5:
        for cont in range(0, len(tabela)):
            print(f'O time {tabela[cont]} está na posição de {cont+1} lugar')
            if cont == 4:
                break
    if opc == 4:
        for cont in range(16, len(tabela)):
         print(f'Os últimos quatro colocados são: {tabela[cont]} na posição de {cont+1} lugar')
    if opc == 3: 
        print(sorted(tabela))
    if opc == 2:
        time = str(input('Qual time você quer saber a colocação atual no brasileirão? '))
        print(f'O time {time} está na posição de {tabela.index(time)+1} lugar')
    if opc == 0:    
        break