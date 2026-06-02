#criar um programa onde o usuário  digite 7 valores numericos e os coloque numa lista única que mantenha separado os valores pares e impares. No final, mostre os valores pares e impares em  ordem crescente
#bora bora
#for c in range(1, 7):
#pra colocar duas listas em uma só desde o começo faça que nem aqui: 
lista1 = [[], []]

for c in range(0,8):
        l = (int(input(f'Digite o {c} valor: ')))
        if l % 2  == 0:
                lista1[0].append(l)
        else:
                lista1[1].append(l)
lista1[0].sort()
lista1[1].sort()
print(f'Números pares: {lista1[0]}')
print(f'Números ímpares: {lista1[1]}')asdadadadaada