matriz = []

# Loop externo: para cada linhas (3 linhas)
for linha in range(3):
    nova_linha = []
    # Loop interno: para cada coluna (3 colunas)
    for coluna in range(3):
        numero = int(input(f'Digite para posição [{linha}][{coluna}]: '))
        nova_linha.append(numero)  # Adiciona à linha atual
    matriz.append(nova_linha)  # Adiciona a linha completa à matriz

# Exibir a matriz
for linha in matriz:
    print(sorted(linha))
    