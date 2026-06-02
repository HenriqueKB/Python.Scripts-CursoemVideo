nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))

nome_comp = nome + " " + sobrenome
print(f"Seu nome completo é {nome_comp}")

cpf = input("Qual seu cpf? ")
quant = len(cpf)
print(f'A quantidade de caracteres no seu cpf é {quant}')

nome_max = nome_comp.upper()
print(f"Seu nome todo maiúsculo é {nome_max}")

nome_min = nome_comp.lower()
print(f"Seu nome todo minúsculo é {nome_min}")

partes = nome_comp.split()
if len(partes) > 1: 
    nome2 = partes[1]
    print(f"Seeu segundo nome é {nome2}")
else:
    print("Não há segundo nome.")