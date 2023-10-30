print("ORDEN DE NÙMEROS")

numeros =  [25, 150, 23, 44, 40, 130, 4]



num_mayor=numeros[0]
num_menor=numeros[0]

for i in numeros:
    if i>num_mayor:
        num_mayor=i
    if i<num_menor:
        num_menor=i

print(f"el numero mayor del arreglo es {num_mayor}")
print(f"el numero menor del arreglo es {num_menor}")