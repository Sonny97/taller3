print("Registro datos personales:")

datosPersonales= {}

preguntas = ["nombre", "apellido", "edad", "Cedula", "tipo de sangre"]

for x in range(5):
    valor = input(f"Ingrese el {preguntas[x]} de la persona: ") 
    datosPersonales[preguntas[x]] = valor

print(datosPersonales)