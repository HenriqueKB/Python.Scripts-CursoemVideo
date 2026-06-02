import math
num= int(input('Digite um número: '))
rzqd= math.sqrt(num)
#math.floor arredonda pra baixo
#math.ceil arredonda pra cima
#para limitar casas decimais só utilizar {:.2f} por ex
print('A raíz quadrada de {} é {:.2f}'.format(num, rzqd))