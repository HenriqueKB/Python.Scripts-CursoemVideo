import random

print("VEJA OS SORTEADOS DA MEGA SENA!")
lista = int(input("Digite quantos jogos vc quer sortear: ")) 

for c in range(1, lista+1):
    megas = random.sample(range(0, 61), 6)
    megas.sort()
    print(f'Jogo {c}: {megas}')