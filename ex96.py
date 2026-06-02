
def calcArea(a, b):
    area = a * b
    print(f'Sua largura é: {a}')
    print(f'Seu comprimento é: {b}')
    print(f'Sua área é: {area}')

a = int(input('Digite a largura do seu terreno:\t'))
b = int(input('Digite o comprimento do seu terreno:\t'))
calcArea(a, b)