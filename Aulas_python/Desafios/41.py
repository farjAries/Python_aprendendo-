#cLASSIFICANDO ATELTAS 
from datetime import datetime
ano = int(input("Ano de nascimento: "))
hoje = datetime.now().year

calculo = hoje - ano
if calculo <= 9:
    classficacao = "MIRIM"
elif calculo <= 14: 
       classficacao = "INFANTIL"
elif calculo <= 19:
        classficacao = "JUNIOR"
elif calculo <= 25:
        classficacao = "SÊNIOR"
else:
        classficacao = "MASTER"

print(f"O atleta tem {calculo}, Classificação: {classficacao}")