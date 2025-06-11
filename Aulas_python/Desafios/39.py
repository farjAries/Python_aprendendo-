
#Alistamento Militar 
from datetime import datetime
Ano = int(input('Ano de nascimento:'))
#sempre ver se tem como usar uma biblioteca 
Ano_atual = datetime.now().year #Ano atual
Ano_maior = Ano + 18 #Ver em que ano a pessoa faz 18
idade = Ano_atual - Ano
Falta = Ano + 18 - Ano_atual

if idade < 18:
    print(f'Quem nasceu {Ano} tem {idade} em {Ano_atual}. Ainda faltam {Falta} anos para o alistamento militar Seu alistamento será em {Ano_maior}')
elif idade == 18:
    print(f"Quem nasceu em {Ano} tem {idade} anos em {Ano_atual} Voce tem que se alistar IMEDIATAMENTE")
    
else:
    print(f'Quem nasceu em {Ano} tem {idade} anos em {Ano_atual}, Voce ja deveria ter se alistado há {Falta * - 1}, Seu alistamento foi em {Ano_maior}')
