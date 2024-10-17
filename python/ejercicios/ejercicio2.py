"""
Suma de pares de números
parametros: lista de números, valor
Dada una lista de numeros, mostrar los pares de números que sumamos obteniendo el valor pasado como parametro.
la funcion además de msotrar los pares de números, devolverá el número de pares de números que suman ese valor
por ejemplo: suma_pares([1,3,2,2],4 ) --> (1,3) (2,2)
"""

def suma_pares(numeros, suma):
    if len(numeros) < 2:
        return
    
    vistos = set() # numeros que van saliendo
    salida = set() # numeros que den el resultado

    for num in numeros:
        objetivo = suma - num
        if objetivo not in vistos:
            vistos.add(num)
        else:
            salida.add( (min(num, objetivo), max (num, objetivo)) )

    for elemento in salida:
        print(elemento)
    
    return len(salida)

# print(suma_pares([1,3,2,2], 4))
# print(suma_pares([1,3,2,2], 3))
print(suma_pares([1], 3))

