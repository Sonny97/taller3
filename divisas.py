print("Bienvenido al buscador de divisas")

divisas = {"dòlar":"$","euro":"€","yen":"¥","libra esterlina":"£","franco suizo":"CHF"}

divisa = input ("ingresar el nombre de la divisa deseada para saber el sìmbolo:").lower()

if divisa in divisas:
    simbolo = divisas[divisa]
    print(f"¡Has aprendida un simbolo nuevo el dìa dde hoy!\n")
    print(f"Nombre de la disisa:{divisa}")
    print(f"Sìmbolo de la divisa:{simbolo}")
else:
    print("Lamentablemente la divisa que buscas no hace parte de nuestro mapa todavìa")

