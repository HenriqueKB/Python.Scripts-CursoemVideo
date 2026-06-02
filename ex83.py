#fazer um  programa que veja se uma expressão está valida se baseaando nas parenteses, se estão fechadas corretamente


exp = str(input('Digite uma expressão matemática com parenteses: '))
pilha = []
for simb in exp:
    if simb == '(': 
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:   
            pilha.append(')')
        break
if len(pilha) == 0:
    print('Sua expressão ta certa')
else:
    print('Ta errado.')