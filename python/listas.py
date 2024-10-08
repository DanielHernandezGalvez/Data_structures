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