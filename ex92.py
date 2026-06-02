listatrab = {'nome': '', 'nasc': 0, 'clt': 0, 'contrat': 0, 'salario': 0, 'aposent': 0, 'gen': ''}
opc = 'S'

listatrab['nome'] = str(input('Digite seu nome: ')).capitalize()
nasc = int(input('Digite seu ano de nascimento: '))
listatrab['nasc'] = 2026 - nasc
listatrab['gen'] = str(input('Digite se é Homem (H) ou Mulher (M): ')).upper()
while opc == 'S':
    opc = str(input('Você possui carteira de trabalho? [Digite S/N]): ')).upper()

    if opc == 'N':
        listatrab['clt'] = 0

        print(f'Nome: {listatrab['nome']}')
        print(f'Idade:  {listatrab['nasc'] }')
        print(f'CLT: NÃO POSSUI')

    if opc == 'S':
        listatrab['clt'] = int(input('Digite sua CLT: '))
        listatrab['contrat'] = int(input('Digite seu Ano de Contratação: '))
        listatrab['salario'] = int(input('Digite seu Salário: '))

        if listatrab['gen'] == 'Ff':
            listabrab['aposent'] = listatrab['contrat'] + 35 - nasc
            print(f'Ano de Aposentadoria: {listatrab['aposent']}')
        else:
            listatrab['aposent'] = listatrab['contrat'] + 40 - nasc

        print('\nDADOS CADASTRAIS DO TRABALHADOR')
        print(f'Nome: {listatrab['nome']}')
        print(f'Idade:  {listatrab['nasc'] }')
        print(f'CLT: {listatrab['clt']}')
        print(f'Ano de Contratação: {listatrab['contrat']}')
        print(f'Salário: {listatrab['salario']} R$')
        print(f'Ano de Aposentadoria: {listatrab['aposent']}')

        break
