print('='*40)
print('{:^40}'.format('BANCO Master'))
print('='*40)
cinquenta = vinte = dez = um = 0
valor = int(input('Qual valor deseja sacar: R$ '))
while valor > 50:
    cinquenta += 1
    valor -= 50
while valor > 20:
    vinte += 1
    valor -= 20
while valor > 10:
    dez += 1
    valor -= 10
while valor >= 1:
    um += 1
    valor -= 1
print(f'Total de {cinquenta} cédulas de R$ 50,00.\nTotal de {vinte} cédulas de R$ 20,00.\n'
      f'Total de {dez} cédulas de R$ 10,00.\nTotal de {um} cédulas de R$ 1,00.')
print('='*40)
print('Volte sempre ao Banco Master! Tenha um bom dia!')