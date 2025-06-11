# CONDIÇOES ANINHADAS

nome = str(input('Qual é seu nome?'))

if nome == 'Fernando':
    print('ola fernando')
elif nome == 'ana' or nome == 'Clark' or nome == 'luis':
    print('Ola')

elif nome in ['marcos', 'andre', 'macaco']:
    print('qual foi')
else:
    print('Quem e voce')   
#o elif funciona se o primeiro if nao estiver verdadeiro e o a configuracao do elif estiver verdadeiro