"""
Operaciones con conjuntos
Crear una función que reciba como parámetro un conjunto de números y devuelva un diccionario con los siguientes resultados:

Longitud del conjunto

Valor máximo del conjunto

Valor mínimo del conjunto

Verificar que el elemento con valor 3 existe en el conjunto

Hacer la intersección con el conjunto {2,3,6}
"""

def operaciones_con_conjuntos(conjunto):
    # Crear el diccionario donde se almacenarán los resultados
    resultados = {}
    
    # Longitud del conjunto
    resultados['Longitud'] = len(conjunto)
    
    # Valor máximo del conjunto
    resultados['Maximo'] = max(conjunto)
    
    # Valor mínimo del conjunto
    resultados['Minimo'] = min(conjunto)
    
    # Verificar si el valor 3 está en el conjunto
    resultados['Existe'] = 3 in conjunto
    
    # Intersección con el conjunto {2, 3, 6}
    conjunto_referencia = {2, 3, 6}
    resultados['Intersección'] = conjunto.intersection(conjunto_referencia)
    
    return resultados