#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

print('BEM VINDO AO PROGRAMA DE SORTEAMENTO E SOMA DE PARES 5000')
sleep(1.0)
def sorteia(listaSort):
    print('Sorteando 5 Valores da Lista: ', end ='')
    for cont in range(0,5):
        sorteio = randint(1,10)
        listaSort.append(sorteio)

        print(f'{sorteio}', end=' ', flush=True)
    sleep(0.3)
    print('\n FEITO!')

def somaPar(listaSort):
    soma = 0
    for n in listaSort:
        if n % 2 == 0:
            soma =+ n
    sleep(0.5)
    print(f'A soma entre os pares da {listaSort} deu {soma}')
    
numeros = list()
sorteia(numeros)
somaPar(numeros)
