#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

aprovt = {'nome': '', 'partidas': 0, 'gols': [], 'cont': 0}
aprovt['nome'] = str(input('Digite o nome do jogador: '))
aprovt['partidas'] = int(input('Quantas partidas ele jogou: '))
for c in range(0, aprovt['partidas']):
    gols_partida = int(input(f'Quantos gols na partida {c+1}: '))
    aprovt['gols'].append(gols_partida)
    aprovt['cont'] += gols_partida
    

print(f'O jogador {aprovt['nome']} fez {aprovt['cont']} gols em {aprovt['partidas']} partidas!')
print()
for c in range(0, aprovt['partidas']):
    print(f'Na partida {c+1} ele fez {aprovt['gols'][c]} gols!')

