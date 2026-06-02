from time import sleep
print('GERADOR DE PA')
sleep(1)
p1 = int(input('Insira o primeiro termo: '))

r = int(input('Ótimo, agora insira a razão: '))
termo = p1
cont = 1
total = 10  # começa mostrando 10 termos
mais = 10   # quantidade de termos a mostrar a cada rodada

while mais != 0:
    while cont <= total:
        print('{}'.format(termo))
        termo += r
        cont += 1
    print('FIM')
    mais = int(input('Quantos termos você quer mostrar a mais? (0 para parar): '))
    sleep(1)
    total += mais  # soma ao total de termos
sleep(1)
print('Progressão finalizada com {} termos mostrados.'.format(cont - 1))