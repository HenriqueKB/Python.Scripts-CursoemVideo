#Ler nome, média e guardar a situação deele, tudo num dicionário, no final mostrar o conteúdo
#CONCLUÍDO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
escola = {'nome': ' ', 'media': 0, 'situacao': ' '}
escola['nome'] = str(input('Digite seu nome: ')).capitalize()
escola['media'] = int(input('Digite sua média: '))

if escola['media'] > 60:
    escola['situacao'] = 'APROVADO!'
else:
    escola['situacao'] = 'REPROVADO!'

print(f'Nome é: {escola['nome']}')
print(f'A média é: {escola['media']}')
print(f'Situação: {escola['situacao']}')