usu = contador = r1 = 0
usu = int(input('Digite o MÁXIMO que quiser, caso queira parar, digite 999: '))
while usu != 999:
  
 
 r1 += usu
 contador  += 1
 usu = int(input('Digite o MÁXIMO que quiser, caso queira parar, digite 999: '))
print('Vc digitou {} números, e a soma entre eles foi: {}'.format(contador, r1))