print("-=" * 20)
print("Analisador de triangulo")
print("-=" * 20)

primeiro = float(input("primeiro segmento: "))
segundo = float(input("Segundo segment: "))
terceiro = float(input("Terceiro segmento: "))

    
if primeiro + segundo > terceiro and primeiro + terceiro > segundo and segundo + terceiro > primeiro:
    print(f"Os segmento acima PODEM FORMAR triangulo!")
else :
    print(f"Os segmento acima NAO PODEM FORMAR triangulo!")
#  eu tinha esqueci de colocar o terceira condição