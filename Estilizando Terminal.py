#ANOTAÇÔES
# O código \033[0;33;44m será a chave para estilizar o terminal, só trocar o número.
# Os códigos pra estilo são 0,1,4,7;
# Os códigos para estilo de texto sãp 30;31;32;33;34;35;36;37; podendo gerar cor preta tbm
# Os códigos para o plano de fundo são 40;41;42;43;44;45;46;47;
# Gerar texto branco com fundo vermelho: \033[0;30;41m
# Gerar texto amarelo com fundo azul: \033[4;33;44m
# Gerar texto branco com fundo pretp: \033[m
# Para fechar o código, use \033[m no final 
print('\033[0;30;41mTeste\033[m') 