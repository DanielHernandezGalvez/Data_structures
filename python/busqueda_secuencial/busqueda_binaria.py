# algoritmo de busqueda binaria en una lista ordenada
# lista = [1,2,3,4,5,6,7]
# busqueda_binaria(20) --> True
# busqueda_binaria(3) --> False

def busqueda_binaria(lista, elemento):
    primero = 0
    ultimo = len(lista) -1
    encontrado = False

    while primero <= ultimo and not encontrado:
        medio = (primero + ultimo) // 2 # da un valor entero
        if lista[medio] == elemento:
            encontrado = True
        else:
            if elemento < lista[medio]:
                ultimo = medio - 1
            else:
                primero = medio + 1

    return encontrado

lista_ordenada = [1,2,4,5,6,7,8,9,12,14]

print(busqueda_binaria(lista_ordenada, 20))


