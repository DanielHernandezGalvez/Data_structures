""" 
Operaciones con listas
Crear una función que reciba como parámetro una lista de números y devuelva una lista con los valores siguientes:

Suma de los elementos de la lista

El valor máximo de la lista

El valor mínimo de la lista

La lista de números ordenada de forma ascendente

La lista con los cuadrados de cada número de la lista
"""


def operaciones_con_listas(lista_numeros):
    # Suma de los elementos de la lista
    suma = sum(lista_numeros)
    
    # Valor máximo de la lista
    valor_max = max(lista_numeros)
    
    # Valor mínimo de la lista
    valor_min = min(lista_numeros)
    
    # Lista de números ordenada de forma ascendente
    lista_ordenada = sorted(lista_numeros)
    
    # Lista con los cuadrados de cada número
    lista_cuadrados = [num ** 2 for num in lista_numeros]
    
    # Retornar todos los resultados en una lista
    return [suma, valor_max, valor_min, lista_ordenada, lista_cuadrados]



