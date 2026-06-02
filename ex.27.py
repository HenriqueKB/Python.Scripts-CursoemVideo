n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome eh {}'.format(nome[0]))
print('Seu ultimo nome eh {}'.format(nome[len(nome)-1]))