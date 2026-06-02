from random import randint
from time import sleep
print('Bem vindo! Você acha que ganha de mim no PEDRA, PAPEL e TESOURA?')
print("-=" * 10)

item= ('Pedra', 'Papel', 'Tesoura')
comp = randint (0, 2)

print("-=" * 10)
user = int(input('''ESCOLHA:
[0] Pedra
[1] Papel
[2] Tesoura
'''))
print("-=" * 10)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
print("-=" * 10)

print("O computador escolheu {}".format(item[comp]))
print("Você escolheu {}".format(item[user]))

print("-=" * 10)
if user == comp:
    print("EMPATE!")    
elif user == 0 and comp == 1:
    print("Papel embrulha Pedra, você perdeu!")    
elif user == 0 and comp == 2:
    print("Pedra esmaga Tesoura, você ganhou!")
elif user == 1 and comp == 2:
    print("Tesoura corta Papel, você perdeu!")
elif user == 1 and comp == 0:
    print("Papel embrulha Pedra, você ganhou!")
elif user == 2 and comp == 0:
    print("Pedra esmaga Tesoura, você perdeu!")
elif user == 2 and comp == 1:
    print("Tesoura corta Papel, você ganhou!")
print("-=" * 10)

ZR8016Y1056_@pOlL07814
jk$HK4GYEaE03zXs
EK12432I_901_yEEoFR4h
