lista = [[], [], [], []]
while True: 
    nome = str(input('Digite o nome do aluno: '))
    lista[0].append(nome)
    nota1 = int(input(f'Digite a nota 1 do {nome}: '))
    lista[1].append(nota1)
    nota2= int(input(f'Digite a nota 2 do {nome}: '))
    lista[2].append(nota2)
    

    media = (nota1 + nota2) / 2 

    lista[3].append(media)
    opc = str(input('Quer continuar? S/N')).upper().strip()
    if opc == 'N':
        break

print('\n-_-_-_-_ALUNOS E SUAS MÉDIAS_-_-_-_-')
for nome, media in zip(lista[0], lista[3]):
    print(f"{nome} e sua media eh {media:.1f}")
while True:
    opc2 = int(input("Qual aluno? (1, 2, 3...) ou 999 para sair: "))

    if opc2 == 999:
        break

    # Converter posição do usuário para índice Python
    indice = opc2 - 1

    # Validar se o índice existe
    if 0 <= indice < len(lista[0]):
        print(f"{lista[0][indice]} - Nota 1: {lista[1][indice]}, Nota 2: {lista[2][indice]}")
    else:
        print("Aluno não existe!")