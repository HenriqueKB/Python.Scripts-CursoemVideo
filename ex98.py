#Exercício Python 098: Faça um programa que tenha uma função chamada #contador(), que receba três parâmetros: início, fim e passo. Seu programa #tem que realizar três contagens através da função criada:

#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep
opc = "S"
def contador(i, m, s):
    print()
    for c in range(i, m, s):
        print(c, end = " ")
    print()

while True: 
    sleep(1)
    print("\n \033[0;31;44mContagem de 1 a 10 com 1 Intervalo:\033[m ")
    contador(1, 11, 1)
    print('FIM')
    print('-'*30)
    sleep(1)
    print("\n \033[0;31;44mContagem de 10 a 0 com 2 Intervalos:\033[m ")
    contador(10, -1, -2)
    print('FIM')
    sleep(1)

    print('-'*30)
    print("\nBem Vindo Ao Programa Contador 3000")
    sleep(1)
    print("FAÇA SUA CONTAGEM PERSONALIZADA: ")
    i = int(input("Digite o começo da contagem: "))
    m = int(input("Digite o final da contagem: "))
    s = int(input("Digite o intervalo da contagem: "))

    print('-'*30)
    print("\n SUA CONTAGEM: ")
    contador(i, m, s,)
    print(end = 'FIM')
    opc = str(input("\n Quer continuar com a contagem? S/N")).upper()
    if opc == "N":
        print("\033[0;30;41mENCERRANDO!\033[m")
        break
