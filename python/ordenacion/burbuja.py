#  lista = 65318624
# primera iteracion
# lista = 65
# lista = 563
# lista = 5361 ...

def ordenacion_burbuja(lista):
    for num in range(len(lista) - 1, 0, -1): # se recorre en orden inverso
        for indice in range(num):
            if lista[indice] > lista[indice + 1]:
                temporal = lista[indice]
                lista[indice] = lista[indice +1]
                lista[indice + 1] = temporal

lista = [2,4,6,3,4,2,56,7,45,3,6,35,33]
ordenacion_burbuja(lista)
print(lista)