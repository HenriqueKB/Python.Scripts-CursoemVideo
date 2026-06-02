nmrextenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

nmr = int(input('Digite um número de 0 a 20: '))
pos = nmr
while nmr <= 21:
    print(f'Você digitou o número {nmrextenso[nmr]}')
    break
if nmr >= 21:
    print('ERRO!')