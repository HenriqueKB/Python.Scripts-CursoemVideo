v = float(input('Digite o valor da casa que irá comprar: '))
s = float(input('Digite seu salário: '))
a = float(input('Quantos anos você quer pagar a casa? '))
p = v / (a * 12)
if p > (s * 0.3):
    print('O valor da casa é {:.2f}, assim a prestação fica {:.2f} em {} anos, e com um salário de {:.2f}, seria impossível pagar isso. Empréstimo negado!'.format(v, p , a, s))
elif p <= (s * 0.3):
    print('O valor da casa é {:.2f}, assim a prestação fica {:.2f} em {} anos, e com um salário de {:.2f}, seria possível pagar isso! Empréstimo aprovado!'.format(v, p, a, s))
