"""
Comprimir una cadena de letras en función de sus repeticiones
comprimir("AAB") --> "A2B1"
comprimir("AAAABBBCCdaaa") --> "A4B3C2D1a3"
"""

def comprimir(cadena):

    resultado = ""
    longitud = len(cadena)

    if longitud == 0:
        return ""
    
    if longitud == 1:
        return cadena + "1"
    
    contador = 1
    i = 1

    while i < longitud:
        if cadena[i] == cadena[i - 1]:
            contador += 1
        else: 
            resultado += cadena[i - 1] + str(contador)
            contador = 1
        i += 1
    
    resultado = resultado + cadena[i-1] + str(contador)

    return resultado

print(comprimir("AAAABBBCCdaaa"))
