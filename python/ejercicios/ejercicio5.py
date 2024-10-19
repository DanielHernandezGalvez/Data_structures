"""
Dadas 2 listas, encontrar los elementos que están en una lista y no están en la otra lista
buscar([1,2,3,4,5,6], [6,3,2,3]) --> [1,5]
buscar([1,2,3,"hola"], [2,3]) --> [1,"hola"]
"""

def buscar(lista1,lista2):
    # return [elemento for elemento in lista1 if elemento not in lista2]  

    resultado = []

    for num in lista1:
        if num not in lista2:
            resultado.append(num)

    for num in lista2:
        if num not in lista1:
            resultado.append(num)

    return resultado

# Clase de pruebas para la función "buscar"
from nose.tools import assert_equal

class Pruebas_buscar(object):
    def test_buscar(self):
        
        assert_equal(buscar([1, 2, 3, 4, 5, 6], [6, 3, 2, 3]), [1, 4, 5])
        assert_equal(buscar([1, 2, 3, "hola"], [2, 3]), [1, "hola"])
        assert_equal(buscar([], [1, 2, 3]), [])
        assert_equal(buscar([1, 2, 3], [1, 2, 3]), [])
        assert_equal(buscar([1, 2, 3], []), [1, 2, 3])
        assert_equal(buscar(["a", "b", "c"], ["b"]), ["a", "c"])

        print("¡Todos los tests pasaron!")

print(buscar([1,2,3,"hola"], [2,3]))

prueba = Pruebas_buscar()
prueba.test_buscar()

