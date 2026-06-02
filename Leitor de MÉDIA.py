n1 = float(input('Digite uma nota sua: '))
n2 = float(input('Digite outra nota sua da mesma matéria: '))
med = (n1 + n2)/2


print('Sua média é {:.2f}'.format(med))
if med < 50:
    print('Sua média foi {:.2f}, portanto, vocé foi reprovado, ESTUDE MAIS!'.format(med))
elif med > 60:
    print('Sua média foi {:.2f}, portanto, vocé foi aprovado, NÃO FEZ MAIS QUE A SUA OBRIGAçãO!'.format(med))
#o comando {:.2f} serve para limitar as casas decimais
elif med >= 50 and med <= 60:
    print('SUa média foi {:.2f}, você não foi reprovado mas precisa melhorar!'.format(med))