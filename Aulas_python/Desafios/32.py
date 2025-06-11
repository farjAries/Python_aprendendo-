from datetime import date

Ano = int(input("Que ano quer analisar? "))
if Ano == 0:
    Ano = date.today().year
# Usar a lógica correta de bissexto
bissexto = (Ano % 4 == 0) and ((Ano % 100 != 0) or (Ano % 400 == 0))

if bissexto:
    print(f"{Ano} É bissexto")
else:
    print(f"{Ano} Não é bissexto")
