
print("{:=^40}".format("Bem vindo às LOJAS HENRIQUE!"))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')

opc = int(input("Qual é a opção?  "))
if opc == 1:
    total = preco - (preco * 10/100)
elif opc == 2:
    total = preco - (preco * 5/100)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, total))
elif opc == 3:
    total = preco / 2
    print("Sua compra de R${:.2f} vai custar duas parcelas de R${:.2f} sem juros".format(preco, total))
elif opc == 4:
    par = float(input('Quantas parcelas? '))
    par2 = preco / par + (preco * 20/100)
    total = par2 * par
    print("Sua compra de R${:.2f} ficará parcelada em {} vezes de R${:.2f}, no final isso lhe custará {:.2f}".format(preco, par, par2, total))