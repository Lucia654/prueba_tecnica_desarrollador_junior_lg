#listado de personas:
personas = {
    "John":"Doe",
    "Jane":None,
    "Jose":"Doe"
    }

#ingreso de apellido a buscar:
BuscarApe = input("Digite el apellido a buscar en la lista: ")

resultado = {}

for clave, valor in personas.items():
    if valor == BuscarApe:
        resultado[clave] = valor

print (resultado)