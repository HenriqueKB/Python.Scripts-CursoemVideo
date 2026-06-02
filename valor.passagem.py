d= int(input('Qual a distância da sua viagem? '))
if d <= 200:
    print('Sua passagem custa R${:.2f}'.format(d*0.50))
else:
    print('Sua passagem custa R${:.2f}'.format(d*0.45))