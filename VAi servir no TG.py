from datetime import date
print('Você tem idade para servir?')
a= int(input('Digite o ano em que nasceu: '))
atual= date.today().year
ans= atual - a
ps= 18 - ans
ass= ans - 18
if ans == 18:
    print('Já pode se alistar filhão')
elif ans < 18:
    print('Ainda não pode se alistar, lhe falta {} anos'.format(ps))
elif ans >  18:
    print('Já passou do tempo de se alistar, já passou {} anos desde o alistamento'.format(ass))