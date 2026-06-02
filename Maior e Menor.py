contador = media = num = soma = 0

soun = str(input('Digite S para sair e C para começar o programa:')).upper()
num = int(input('Digite um número: '))
contador += 1
soma += num
maior = num
menor = num
if num > maior:
    maior = num
elif num < menor:
    menor = num

while soun == 'C':

 num = int(input('Digite um número: '))
 contador += 1
 soma += num
 soun = str(input('Digite S para sair e C para continuar o programa: ')).upper()


  
 if num > maior:
    maior = num
 elif num < menor:
    menor = num
    
media = soma / contador


 

 
print('\nVc digitou {} números, e a média foi {} \nO maior valor foi {} e o menor foi {}.\nA soma total foi {}.'.format(contador, media, maior, menor, soma))
