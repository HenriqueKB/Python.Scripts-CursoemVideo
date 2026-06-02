#PEGAR O DESAFIO 93 PARA ELE RODAR COM VÁRIOS JOGADORES, COM UM SISTEMA DE VISUALIZAÇÃO DE APROVEITAMENTO DE JOGADOR



opc = 'S'
#PROCESSAMENTO
aprovt = {'nome': '', 'partidas': 0, 'gols': [], 'cont': 0}
lista4 = []
while opc == 'S':
    aprovt['nome'] = str(input('Digite o nome do jogador: '))
    aprovt['partidas'] = int(input('Quantas partidas ele jogou: '))
    for c in range(0, aprovt['partidas']):
        gols_partida = int(input(f'Quantos gols na partida {c+1}: '))
        aprovt['gols'].append(gols_partida)
        aprovt['cont'] += gols_partida
    lista4.append(aprovt.copy())
    aprovt['gols'] = []
    aprovt['cont'] = 0
    opc = str(input('Quer continuar? S/N: ')).upper()
    if opc == 'N':
        break

#IMPRESSÃO
print(f'\n OS jogadores cadastrados foram {len(lista4)}: ')
for i, v in enumerate(lista4):
    print(f"\n Jogador {v['nome']}")

while True:
    opc2 = int(input("Qual jogador? (1, 2, 3...) ou 999 para sair: "))

    if opc2 == 999:
        break

    # Converter posição do usuário para índice Python
    indice = opc2 - 1

    # Validar se o índice existe
    if opc2 >= len(lista4):
        print(f'ERRO! O JOGADOR NÃO EXISTE com o código {opc2}')
    else:
            print(f'O jogaodr {lista4[opc2]['nome']} teve o seguinte aproveitamento: ')
            print()
            for i, g in enumerate(lista4[opc2]['gols']):
                print(f'\033[0;30;41mNo jogo {i+1} fez: {g} gols\033[m')
                ('\033[0;30;41mTeste\033[m')
    print('-'* 40)
