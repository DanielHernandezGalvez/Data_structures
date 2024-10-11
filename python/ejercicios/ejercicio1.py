"""
Verificar si una palabra es anagrama de otra
una palabra es anagrama de otra si tiene las mismas letras, el mismo número de veces,
pero en distinto orden.
por ejemplo: ("paris", "prisa")
"""

def anagrama(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()