n = s = cont = 0
while True:
    n = int(input('Digite um número [Para encerrar digite 999]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'O resultado da soma é {s} e {cont} números foram digitados.')