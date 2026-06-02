matriz = []
s = 0
s3 = 0 
# Loop externo: para cada linhas (3 linhas)
for linha in range(3):
    nova_linha = []
    # Loop interno: para cada coluna (3 colunas)
    for coluna in range(3):
        numero = int(input(f'Digite para posição [{linha}][{coluna}]: '))
        #if numero == 0: #a partir do PRIMEIRO VALOR QUE EU DIGITO, ele JA é o MAIOR E MENOR.
        #mai = men = numero
        
        nova_linha.append(numero)  # Adiciona à linha atual
    matriz.append(nova_linha)  # Adiciona a linha completa à matriz

# Exibir a matriz
for linha in matriz:
    print((linha))

#soma entre os pares
    for l in linha: 
        if l % 2 == 0:
            s += l
print((s))
#eu te odeio indentação do python.

#agr devo fazer soma entre os caras da 3a coluna::
for linha in matriz:
        s3 += linha[2]
print((s3))

#ja que o codigo eh linha por linha, tenho que tecnicamente peggar o 3o valor de cada linha para assim pegar os 3 valores da 3a colunna, vamos ver. DEU CERTO KKKKKKKKKKKKKKKKKKKKKKKKKKKKK]
#if numero > maior:
#    mai = num
# elif numero < menor:
#    men = num
#agr tenho que comparar e achar o maior num da segunda linha:

valor_max2 = max(matriz[1])
print(valor_max2)