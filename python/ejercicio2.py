"""
Operaciones con tuplas


Se pide crear una función que reciba como parámetro una tupla y devuelva otra tupla con los siguientes resultados:

Primer elemento de la tupla

Tercer elemento de la tupla

Longitud de la tupla

Verificar si el número 3 está en la tupla

"""

def operaciones_con_tuplas(tupla_numeros):
    # Primer elemento de la tupla
    primer_elemento = tupla_numeros[0]
    
    # Tercer elemento de la tupla (si tiene al menos 3 elementos)
    tercer_elemento = tupla_numeros[2] if len(tupla_numeros) > 2 else None
    
    # Longitud de la tupla
    longitud = len(tupla_numeros)
    
    # Verificar si el número 3 está en la tupla
    contiene_tres = 3 in tupla_numeros
    
    # Devolver una tupla con los resultados
    return (primer_elemento, tercer_elemento, longitud, contiene_tres)
