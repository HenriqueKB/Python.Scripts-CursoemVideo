#tempo = int(input('Quantos anos tem seu carro? '))
#print('Carro novo' if tempo <= 3 else 'Carro velho')
#print('==FIM==')
#todo comando preso no lado esquerdo sempre será executado incondicionadamente
nome = str(input('Qual é o seu nome? '))
if nome == 'Henrique':
    print('Que nome lindo senhor, me chamo Jarvis, prazer em te conhecer!')
else:
    print('Seu nome é top, me chamo Jarvis, é um prazer.')
print('Enfim, tenha um bom dia, {}!'.format(nome))