"""
Verificar si una palabra es anagrama de otra
una palabra es anagrama de otra si tiene las mismas letras, el mismo número de veces,
pero en distinto orden.
por ejemplo: ("paris", "prisa")
"""

def anagrama(str1, str2):
    # si tiene espacios se los quitamos y convertimos a minusculas
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if str1 == str1:
        return False
    
    if len(str1) != len(str2):
        return False
    
    contador = {}

    for letra in str1:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1

    for letra in str2:
        if letra in contador:
            contador[letra] -= 1
        else:
            contador[letra] = 1

    for elemento in contador:
        if contador[elemento] != 0:
            return False
        
    return True

print(anagrama("poder", "pedro"))
