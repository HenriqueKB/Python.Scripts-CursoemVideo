v= int(input('Digite a velocidade que você estava dirigino no momento da multa: '))
if v > 80:
    m = (v - 80) * 7
    print('Vocé foi multado em R${:.2f}'.format(m))
else:
    print('Vocé estava dentro do limite de velocidade!')