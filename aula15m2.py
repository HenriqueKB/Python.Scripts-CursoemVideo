n = s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    cont += 1
    if n == 999:
        break
    s += n
print(f'A SOMA VALE {s}')