for c in range (1,5):

    print('{} Pessoa'.format(c))
    nome = str(input('Digite o nome: ')).strip()
    sexo = str(input('Digite M para Masculino e F para Feminino: ')).strip()
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite seu peso: '))

mediai = idade / 4 
#somai += idade

mediap = peso / 4
#somap += idade
print('A média de idade do grupo é {} anos.'.format(mediai))
print('A média de peso do grupo é {} kilos.'.format(mediap))
