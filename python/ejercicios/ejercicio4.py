"""
Dadas 2 listas de números, verificar que son iguales, que contienen los mismos valores
devolver True si son iguales, y False si son distintas
iguales([1,2,3,4,5,6], [6,5,4,3,2,1]) --> True
iguales([1,1,2,4,5,6], [1,1,3,4,5,6]) --> False
"""

def iguales(lista1, lista2):
    
    if len(lista1) != len(lista2):
        return False
    
    lista1.sort() # esto es para ordenar las listas
    lista2.sort()

    for num1, num2 in zip(lista1, lista2): # zip las hace de este modo (1,1), (1,2), (2,3)...
        if num1 != num2:
            return False
        else:
            return True

    # print(lista1, " ", lista2 )

print(iguales([1,2,3,4,5,6], [6,5,4,3,2,2,1]))
