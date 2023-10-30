productos = ["Espaguetis", "Salchichon", "Chorizo", "Pollo", "Azúcar", "Arroz", "Sal"]
precios = [3000, 7150, 12000, 5000, 3500, 2000, 1500]

Diccionario_productos =  {}

for x in range(len(productos)):
    Diccionario_productos[productos[x]] =  precios[x]

print(Diccionario_productos)

