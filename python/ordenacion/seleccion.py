# lista = 65342345
# ordena desde el valor mas alto al mas bajo y lo manda a la derecha

def ordenacion_seleccion(lista):
    for numero in range(len(lista) -1, 0, -1):
        indice_max = 0
        for indice in range(1,numero +1):
            if lista[indice] > lista[indice_max]:
                indice_max = indice

        temporal = lista[numero]
        lista[numero] = lista[indice_max]
        lista[indice_max] = temporal

lista = [1,6,4,7,9,6,43,23,52,7,2]
ordenacion_seleccion(lista)
print(lista)
