salario = float(input("Quanto voce ganha? "))

if salario >= 1250:
    dez = salario + (salario * 10  / 100)
    print(f"o seu salario é {salario}, com 10% de aumento passa a ser {dez:.2f} ")
else:
    quinze = salario + (salario * 15  / 100) 
    print(f"Seu salario é {salario}, com 15%  de aumento passa a ser {quinze:.2f} ")
