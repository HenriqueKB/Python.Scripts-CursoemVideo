from datetime import date 
atual = date.today().year


totc= 0
toti= 0
tota= 0
for c in range(1, 8):
    i= int(input('Digite o ano em que nasceu: '))
    idade = atual - i

    if idade >= 80:
        toti += 1
       
    if idade  <= 12:
        totc += 1

    if idade >= 30:
        tota += 1

print('Temos {} adultos'.format(tota))
print('Temos {} crianças'.format(totc))
print('Temos {} idosos'.format(toti))

    