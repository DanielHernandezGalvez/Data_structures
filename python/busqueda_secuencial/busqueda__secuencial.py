# Algoritmo de busqueda secuencial

def busqueda_secuencial(lista, elemento):
    posicion = 0
    encontrado  = False

    while posicion < len(lista) and not encontrado:
        if lista[posicion] == elemento:
            encontrado = True
        else:
            posicion += 1

    return encontrado

lista = [1,4,3,6,2,3,4,5,4]

elemento = 9

print(busqueda_secuencial(lista, elemento))
