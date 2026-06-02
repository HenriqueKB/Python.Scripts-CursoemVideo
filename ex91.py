from random import randint
from time import sleep

#importamento de funções e afins.
#podia ter usado from operator import itemgetter pra pegar os resultados, mas a sugestão da ia parece melhor do que a do guanaba.

jogo = {'jogador_1': randint(0,6), 'jogador_2': randint(0,6), 'jogador_3': randint(0,6), 'jogador_4': randint(0,6)} #ez demais
for k,v in jogo.items(): #curiosamente, aqui o elemento jogo.items() é uma tupla, ou seja, podia usar sorted(), mas eu nn sabia.
    sleep(1)             #pra deixar dramático
    print(f'O jogador {k} tirou {v} no dado') 

#aqui pra baixo eu fiz com ajudinha de IA, mal sabia que seria isso
print("\nRANKING")
ranking = sorted(jogo.items(), key = lambda x: x[1], reverse=True)  #o reverse=True eh pra ficar na ordem Maior pra Menor;
                                                                    #o key = lamba x: x[1] eh pra ordena pelo SEGUNDO elemento de cada tupla (o valor do dado) conforme disse claudioia
                                                                    #com itemgetter ficaria: resultado = sorted(jogo.items(), key = itemgetter(1)) # o 1 no indice eh pra pegar os valores nums.
for posicao, (k,v) in enumerate(ranking, 1):
    print(f'{posicao}o Lugar: O jogador {k} tirou {v}')
#resultado final.