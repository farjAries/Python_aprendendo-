#Media de nota
Nota_primeiro = float(input("Primeira nota: "))
Nota_segundo = float(input("Segunda nota: "))
numero = (Nota_primeiro + Nota_segundo) / 2
arredondado = round(numero, 1)


if numero < 5:
    print(f"""Tirando {Nota_primeiro} e {Nota_segundo}, a média do aluno  é {arredondado}
o aluno esta em \033[31mREPROVADO\033[0m.""")

elif numero <= 6:
    print(f"""Tirando {Nota_primeiro} e {Nota_segundo}, a média do aluno  é {arredondado}
o aluno esta em \033[31mRECUPERAÇAO\033[0m""")
    
else: 
    print(f"""Tirando {Nota_primeiro} e {Nota_segundo}, a média do aluno  é {arredondado}
o aluno esta em \033[32mAPROVADO\033[0m.""")