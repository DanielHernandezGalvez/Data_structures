colores = ["rojo", "amarillo", "verde"]

colores[2] = "azul"

len(colores)

colores.append("naranja")

colores.remove("rojo")

# for color in colores:
#     print(color)

colores.clear()

# print(colores)  # imprime "rojo"


# TUPLAS

tupla_colores = ("rojo", "verde", "amarillo")
# print(tupla_colores)

# for color in tupla_colores:
    # print(color)

# a una tupla no se le pueden quitar ni agregar elementos

# print(len(tupla_colores))


# Conjuntos

conjunto_colores = {"rojo", "verde", "azul"}
# print(conjunto_colores)

for color in conjunto_colores:
    print(color)

conjunto_colores.add("negro")

conjunto_colores.remove("verde")

print(conjunto_colores)

#diccionario

diccionario_colores = {"red": "rojo", "blue": "azul", "yellow": "amarillo"}
print("diccionarios")
print(diccionario_colores["red"])

valor = diccionario_colores["yellow"]

diccionario_colores["black"] = "negro"

diccionario_colores.pop("yellow")

del(diccionario_colores["black"])

for color in diccionario_colores:
    print(color)

for clave,valor in diccionario_colores.items():
    print(clave,valor)

print(diccionario_colores)
