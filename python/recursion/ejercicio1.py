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

from nose.tools import assert_equal
class TestReves(object):
    def test_reves(self):
        assert_equal(reves("abc"), "cba")
        assert_equal(reves("hola"), "aloh")
        assert_equal(reves("123"), "321")
        print('test pasados correctamente')

p = TestReves()
p.test_reves()  # run the tests