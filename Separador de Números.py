def separar_numero(numero):
    """ Separa um número em suas dezenas, centenas, milhares, etc. """
    numero = str(numero)
    resultado = []
    for i, digito in enumerate(reversed(numero)):
        if i % 3 == 0 and i != 0:
            resultado.append(".")
        resultado.append(digito)
    return "".join(reversed(resultado))

numero = int(input("Digite um número: "))
print(separar_numero(numero))
