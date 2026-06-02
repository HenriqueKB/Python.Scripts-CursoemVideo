#As condições aninhadas são quando colocamos uma coisa na outra, esta será a função de adicionar mais condições..
#Isso basicamente coloca mais condições além de if e else
#Porque caso precisarmos de MAIS condições além de duas num código, precisaremos usar esta função.

#Ficaria assim, se um carro tivesse três caminhos para percorrer, seria representado assim num código:
#carro siga() #ISSO REPRESENTA O PRiMEIRO CAMINHO
#se carro.esquerda()
#carro.siga()
#carro.direita()
#carro.siga()
#carro.direita()
#carro.esquerda()
#carro.siga()
#carro.direita()
#carro.siga()

#O PRÓXIMO CAMINHO ESTÁ REPRESENTADO ABAIXO
#senão se carro direita()
#carro.siga()
#carro.esquerda()
#carro.siga()
#carro.esquerda()
#carro.siga

#TEMOS AQUI 3 COMANDOS IMPORTANTES!
#Senão se: elif
#se: if
#senão: else

#EXEMPLO PRÁTICO:

nome = str(input('Qual é seu nome?'))
if nome == 'Henrique':
    print('Seja bem vindo meu nobre, o senhor possui um lindo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seja bem vindo(a)! Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claúdia Oliveira dos Santos':
    print('Seja bem vinda, você tem um belo nome feminino!')
else:
    print('Seja bem vindo! Seu nome é bem normal!')
print('Tenha um excelente dia, {}!').format(nome))     
