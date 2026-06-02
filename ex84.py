galera = list()
dado = list()
pesado = list()
leve = list()
mai = cont = 0
men = float('inf')
while True:
        dado.append(str(input('Nome: ')))
        dado.append(int(input('Peso: ')))
        galera.append(dado[:])
        cont += 1
        dado.clear()
       
        opc = str(input('Quer continuar? [S/N]')).upper().strip()
        
        if opc == 'N':
            break   
 
for pessoa in galera:
    if pessoa[1] > mai:
        pesado.clear()
        mai = pessoa[1]
        pesado.append(pessoa)
    elif pessoa[1] == mai:
            pesado.append(pessoa)

    if pessoa[1] < men:
        leve.clear()
        men = pessoa[1]
        leve.append(pessoa)
    elif pessoa[1] == men:
        leve.append(pessoa)
        
print(f'Essa é a galera que vc cadastrou: {galera}')
print(f"Você cadastrou {cont} pessoas")
print("Os mais pesados são:")
for pessoa in pesado:
    print(f"  - {pessoa[0]} com {pessoa[1]}kg")
print("Os mais leves são:")
for pessoa in leve:
    print(f"  - {pessoa[0]} com {pessoa[1]}kg")


#o que fazer:
#qnts pessoas foram cadastradas?
#listagem com as pessoas mais pesadas
#listagem com as pessoas mais leves
#e se as pessoas tiverem o mesmo peso, devo mostrar ambas no final (ex: os mais pesados são joao e marcos com 190kg)