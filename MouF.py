sexo = str((input("Digite seu sexo: "))).strip().upper()[0]

while sexo not in "MF":
    sexo = str((input("Dados incorretos. Tente novamente: "))).strip().upper()[0]
print("Sexo {} registrado com sucesso.".format(sexo))