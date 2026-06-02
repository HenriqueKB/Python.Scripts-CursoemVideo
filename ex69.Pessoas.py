idade = conth = contm = contp = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade > 18:
            contp += 1     
    if sexo == 'M':
            conth += 1
    if sexo == 'F' and idade < 20:
            contm += 1
    encerrar = str(input('Deseja encerrar o programa? [S/N]')).strip().upper()[0]
    if encerrar == 'S':
        break
print(f'{contp} pessoas tem mais de 18 anos, {conth} homens foram cadastrados e {contm} mulheres abaixo de 20 anos foram cadastradas.')