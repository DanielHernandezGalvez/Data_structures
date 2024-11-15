"""
dar la vuelta a una cadena de forma recursiva
construir una clase de prueba
reves("abc") --> "cba"
reves("123") --> "321"
"""

def reves(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return reves(cadena[1:]) + cadena[0]
    
print(reves("123"))