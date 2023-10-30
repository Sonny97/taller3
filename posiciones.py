
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ordenNumeros= sorted(numeros, reverse=True)
cadenaDeNumeros = ', '.join(map(str, ordenNumeros))

print("Nùmeros ordenados de mayor a menor:", cadenaDeNumeros)