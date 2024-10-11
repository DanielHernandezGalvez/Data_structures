"""
Operaciones con diccionarios
Crear una función que reciba como parámetro un diccionario, y que devuelva otro diccionario con estos calculos realizados:

Calcular la cantidad de elementos en el diccionario.

Encontrar las claves y valores máximos y mínimos en el diccionario.

Calcular la suma de todos los valores en el diccionario.

Crear un nuevo diccionario con las claves en mayúsculas y los valores al cuadrado.
"""

def operaciones_con_diccionarios(diccionario):
    # Crear el diccionario donde se almacenarán los resultados
    resultados = {}

    # Calcular la cantidad de elementos en el diccionario
    resultados['Cantidad de elementos'] = len(diccionario)

    # Encontrar la clave asociada al valor máximo y mínimo
    clave_maxima = max(diccionario, key=diccionario.get)
    clave_minima = min(diccionario, key=diccionario.get)
    
    resultados['Clave máxima'] = clave_maxima
    resultados['Valor máximo'] = diccionario[clave_maxima]
    
    resultados['Clave mínima'] = clave_minima
    resultados['Valor mínimo'] = diccionario[clave_minima]

    # Calcular la suma de todos los valores en el diccionario
    resultados['Suma de valores'] = sum(diccionario.values())

    # Crear un nuevo diccionario con claves en mayúsculas y valores al cuadrado
    diccionario_modificado = {clave.upper(): valor**2 for clave, valor in diccionario.items()}
    resultados['Diccionario modificado'] = diccionario_modificado

    return resultados
