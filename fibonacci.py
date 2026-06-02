f1 = 1
f2 = 2
cont = 1
total = 10  # começa mostrando 10 termos
mais = 10   # quantidade de termos a mostrar a cada rodada

while mais != 0:
    while cont <= total:
        print(f1)
        proximo = f1 + f2
        f1, f2 = f2, proximo
        cont += 1
    print('FIM')
    mais = int(input('Quantos termos você quer mostrar a mais? (0 para parar): '))
    
    total += mais  # soma ao total de termos

print('Progressão finalizada com {} termos mostrados.'.format(cont - 1))