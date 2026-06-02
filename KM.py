n1= float(input('Digite uma medida em metros:',))
#jeito melhor dedefinir cores no código:
cores = {
'limpa ':'\033[m', 
'azul':'\033[34m', 
'amarelo':'\033[33m',   
'pretoebranco':'\033[7:30m'}

mm= n1*1000
cm= n1*100
km= n1/1000

print('Seu valor em centímetros é: {} e o seu valor em kilômetros é:\033[m {}, e seu valor em milímetros é:\033[m {}'.format(cores['azul'],cm,km,mm, cores['azul']))