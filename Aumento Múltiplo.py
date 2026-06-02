s= float(input('Digite seu salário atual para iniciar o cálculo:'))

if s<= 1250:
    n= s + (s * 10/100)
else:
    n= s + (s * 15/100)
print('\033mSeu salário com o aumento ficará: {:2}'.format(n))
