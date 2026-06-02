n = tabuada = 0
while True:
 n = int(input('\nDigite um número para revelar sua tabuada: '))
 if n < 0:
  break
 for c in range (1, 11):
    tabuada =  n * c
    print(f'\n {n} x {c} = {tabuada}', end = ' ')
 
 