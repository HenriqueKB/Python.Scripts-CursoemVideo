import random
from time import sleep
n1 = n2 = P = I = s = cont = 0 
a = 0

while True:
 print("Acha que consegue ganhar de mim no Par ou Ímpar?")
 n1 = random.randint(1, 10)
 n2 = int(input('Digite um número: '))
 a = str(input('Digite P para par e I para impar: ')).upper().strip()
 s = n1 + n2
 print(f'\n{n1} + {n2} = {s}', end = ' ')

#condições

#condição par
 if s % 2 == 0 and a == "P":
     print('\nDeu PAR!')
     print('\nParabéns, você ganhou! Bora outra?')
     cont += 1

#condição impar
 elif s % 2 != 0 and a == "I": 
     print('\nDeu ÍMPAR!')
     print('\nParabéns, você ganhou! Bora outra?')
     cont += 1

#condição derrota
 else:
    print(f'\nVocê perdeu! Você ganhou {cont} rodadas!') 
    break        