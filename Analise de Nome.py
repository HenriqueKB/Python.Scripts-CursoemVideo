n= input('Coloque seu nome: ')
print('Seu nome em letra maiuscula eh',n.upper())
print('Seu nome em letra minuscula eh',n.lower())

espacos= n.count(' ')
indice= len(n)
#o len eh usado aq
print('Seu nome tem {} letras'.format(indice-espacos))

dividido= n.split()
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))

print('Seu segundo nome tem {} letras'.format(len(dividido[1])))

print('Seu terceiro nome tem {} letras'.format(len(dividido[2])))