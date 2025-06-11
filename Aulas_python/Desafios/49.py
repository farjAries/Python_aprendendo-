Valor = int(input("Digite um número para ver sua tabuada: "))

for tabuada in range(1,11):
    vezes = Valor * tabuada
    print(f"{Valor} X {tabuada} = {vezes}")
    # UMA OUTRA FORMA DE FAZER ISSO É print(f"{Valor} X {tabuada} = {Valor * tabuada}")
    # ia dar o mesmo resultado
    

