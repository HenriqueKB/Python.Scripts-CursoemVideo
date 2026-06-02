print("Bem vindo à CALCULADORA DE IMC 5000")
altura = float(input("Comece informando sua Altura: "))
peso = float(input("Agora me informe seu peso: "))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Seu IMC é {:.2f}, você está MAGRO". format(IMC))
if IMC >= 18.5 and IMC <=  24.9:
    print("Seu IMC é {:.2f}, você está NORMAL". format(IMC))    
if IMC >= 25 and IMC <= 29.9:
    print("Seu IMC é {:.2f}, você está SOBREPESO". format(IMC))
if IMC >= 30 and IMC <= 34.9:
    print("Seu IMC é {:.2f}, você está com OBESIDADE GRAU I". format(IMC))
if IMC >= 35 and IMC <= 39.9:
    print("Seu IMC é {:.2f}, você está com OBESIDADE GRAU II". format(IMC))
