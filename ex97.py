#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

#Ex: 
#Saída:
#~~~~~~~~~
# Olá, Mundo!
#~~~~~~~~~

def printSpec(msg, simb):
    i  =  len(msg)
    print(f'{simb *i}'.center(50))
    print(f'{msg}'.center(50))
    print(f'{simb *i}'.center(50) )
msg = str(input('Digite qualquer coisa: '))
simb = str(input('Digite um símbolo (=,~,#,@): ')).strip()
printSpec(msg, simb)