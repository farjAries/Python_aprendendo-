numero_1 = int(input("Primeiro numero:"))
numero_2 = int(input("Segundo numero:")) 

if numero_1 > numero_2:
    print("Primeiro é o maior")
elif numero_2 > numero_1:
    print("Segundo é o maior")
elif numero_1 == numero_2:
    print("Os dois Valores sao IGUAIS")
else:
    print("Nao entendi digite novamente")