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

from nose.tools import assert_equal

class TestComprimir:
    
    def test_cadena_normal(self):
        assert_equal(comprimir("AAB"), "A2B1")
        assert_equal(comprimir("AAAABBBCCdaaa"), "A4B3C2d1a3")
    
    def test_cadena_vacia(self):
        assert_equal(comprimir(""), "")
    
    def test_un_solo_caracter(self):
        assert_equal(comprimir("A"), "A1")
    
    def test_sin_repeticiones(self):
        assert_equal(comprimir("ABC"), "A1B1C1")
    
    def test_mayusculas_minusculas(self):
        assert_equal(comprimir("aAaA"), "a1A1a1A1")

print(comprimir("AAAABBBCCdaaa"))

# Ejecutar los tests
if __name__ == '__main__':
    t = TestComprimir()
    t.test_cadena_normal()
    t.test_cadena_vacia()
    t.test_un_solo_caracter()
    t.test_sin_repeticiones()
    t.test_mayusculas_minusculas()
    
    print("Todos los tests pasaron correctamente.")

