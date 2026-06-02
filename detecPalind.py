frase = str(input('Digite uma frase: ')).strip().upper()
palind= frase.split()
junto= ''.join(palind)
inverso= ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('O inverso de {} é {}.'.format(junto, inverso))
    print('\033[32mA frase é um palíndromo\033[m')
else:
    print('\033[31mA frase não é um palíndromo\033[m')