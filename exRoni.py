# Criar uma lista de participantes para um churrasco.
# Os participantes devem ser inseridos através do teclado.
# Será sorteado um organizador que vai organizar mas não vai pagar o churrasco.
# Cadastrar os participantes do lado que vc está do lab (lado esquerdo ou direito).
# Ordenar a lista dos participantes.
# Retirar o organizador da lista.
# Imprimir a quantidade total de participantes da lista.


import random  



def cadastrar_participantes():
    """
    Esta função solicita ao usuário que digite nomes de participantes.
    Cada nome é adicionado a uma lista até que o usuário digite 'sair'.
    """
    participantes = []  =
    
    print("\n" + "="*50)
    print("CADASTRO DE PARTICIPANTES DO CHURRASCO")
    print("="*50)
    print("Digite os nomes dos participantes (ou 'sair' para terminar):\n")
    
    while True:  =
        nome = input("Nome: ").strip()  
        if nome.lower() == 'sair':  
            break
        
        if nome: 
            participantes.append(nome) 
            print(f"✓ {nome} adicionado(a)!")
    
    return participantes 

def ordenar_participantes(lista):
    """
    Esta função organiza os nomes em ordem alfabética.
    O parâmetro 'lista' é a lista de participantes.
    """
    lista_ordenada = sorted(lista) 
    return lista_ordenada



def sortear_organizador(lista):
    """
    Esta função escolhe aleatoriamente um participante para ser o organizador.
    Usa 'random.choice()' que seleciona um elemento aleatório da lista.
    """
    organizador = random.choice(lista) 
    return organizador




def remover_organizador(lista, organizador):
    """
    Esta função remove o organizador da lista de pessoas que vão pagar.
    Cria uma nova lista SEM o organizador.
    """
    lista_pagadores = [nome for nome in lista if nome != organizador]
    return lista_pagadores




def calcular_valor_por_pessoa(valor_total, quantidade_pagadores):
    """
    Esta função divide o custo total entre os pagadores.
    Se não houver pagadores, retorna 0.
    """
    if quantidade_pagadores == 0:  
        return 0
    
    valor_por_pessoa = valor_total / quantidade_pagadores 
    return valor_por_pessoa



def exibir_resultado(participantes, organizador, pagadores, valor_total):
    """
    Esta função exibe todas as informações de forma organizada.
    Mostra o total de pessoas, quem organiza e quanto cada um paga.
    """
    
    print("RESULTADO FINAL DO CHURRASCO")
    print()
    
   
    print(f"\n TOTAL DE PARTICIPANTES: {len(participantes)}")
    
    print(f"\n PARTICIPANTES (em ordem):")
    for i, nome in enumerate(participantes, 1):
        print(f"   {i}. {nome}")
    
    print(f"\n ORGANIZADOR (NÃO PAGA): {organizador}")
    
    if valor_total > 0:
        valor_por_pessoa = calcular_valor_por_pessoa(valor_total, len(pagadores))
        print(f"\n VALOR TOTAL: R$ {valor_total:.2f}")
        print(f"   Dividido por {len(pagadores)} pessoas")
        print(f"   CADA UM PAGA: R$ {valor_por_pessoa:.2f}")
        
        
        print(f"\n QUEM VAI PAGAR:")
        for i, nome in enumerate(pagadores, 1):
            print(f"   {i}. {nome} - R$ {valor_por_pessoa:.2f}")
    
    print("\n" + "="*50)




if __name__ == "__main__":
    
    participantes = cadastrar_participantes()
    
    if len(participantes) < 2:
        print("\n Erro! Precisa de pelo menos 2 participantes!")
        exit()  
    
    
    participantes = ordenar_participantes(participantes)
    
    organizador = sortear_organizador(participantes)
    
    pagadores = remover_organizador(participantes, organizador)
    
    print()
    valor_total = float(input("Qual foi o valor TOTAL do churrasco? R$ "))
    
    exibir_resultado(participantes, organizador, pagadores, valor_total)
    
    print("\n Bom churrasco!")