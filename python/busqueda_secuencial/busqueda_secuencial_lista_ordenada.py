def busqueda_secuencial_ordenada(lista, elemento):
    posicion = 0
    encontrado = False
    parar = False

    while posicion < len(lista) and not encontrado and not parar:
        if lista[posicion] == elemento:
            encontrado = True
        else:
            if lista[posicion] > elemento:
                parar = True
            else:
                posicion += 1
    
    return encontrado

lista_ordenada = [1,2,4,5,6,7,8,9,12,14]



print(busqueda_secuencial_ordenada(lista_ordenada, 3))