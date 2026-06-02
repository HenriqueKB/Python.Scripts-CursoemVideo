from datetime import date
print('Verfique sua CLASSIFICAÇÂO NO ATLETISMO!')
i = int(input('Digite o ano no qual você nasceu: '))
a =  date.today().year
ia= i - a
if ia <=14:
    print('Você tem {} anos será da turma SUB14!'.format(ia))
elif ia <=17:
    print('Você tem {} anos e será da equipe SUB17!'.format(ia))
elif ia <=21:
    print('Você tem {} anos e fará parte da equipe SUB21!'.format(ia))