#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def funcaoMaior (*valores): #O * na definição eh: "receba quantos números forem passados, e organize-os em uma tupla chamada valores"
    if not valores:  # Se nenhum valor foi passado
        print("Nenhum valor foi fornecido!")
        return None
    
    maior = valores[0]  # Começa com o primeiro valor
    for num in valores:
        if num > maior:
            maior = num
    #a função pega desde o primeiro valor digitado e vai comparando um com o outro resumidamente.
    
    print(f"Seu maior número é {maior}")
    return maior

#Eu tinha tentando usar dict, mas esta ideia realmente foi idiotice minha, achei que ia ser legal mas a lista se provou melhor pra esse exercício, muita complicação pra uma coisa simples.
#ou seja, agora ele roda.

print('_-_' *40)
print("BEM VINDO AO PROGRAMA COMPARADOR 3000!")
print('_-_' *40)
lista = []

while True:
    i = int(input("\n Digite seus valores: "))
    lista.append(i)
    opc = str(input("Quer encerrar agora? S/N: ")).upper()
    if opc == 'S':
        break

# Passa todos os números como parâmetros individuais
resultado = funcaoMaior(*lista)
print('_-_' *40)
print(f'\n Os valores digitados foram {lista}, e o maior valor foi {resultado}')
print('_-_' *40)