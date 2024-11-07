class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.nodo_siguiente = None

    def __str__(self):
        return f"Nodo({self.valor}) -> {self.nodo_siguiente}"
    
nodo1 = Nodo("valor 1")
nodo2 = Nodo("valor 2")
nodo3 = Nodo("valor 3")

nodo1.nodo_siguiente = nodo2
nodo2.nodo_siguiente = nodo3

print(nodo1.nodo_siguiente)
print(nodo2.nodo_siguiente)
print(nodo3.nodo_siguiente)

import unittest

class TestNodo(unittest.TestCase):
    def test_creacion_nodo(self):
        # Prueba de creación de un nodo
        nodo = Nodo("valor 1")
        self.assertEqual(nodo.valor, "valor 1")
        self.assertIsNone(nodo.nodo_siguiente)

    def test_enlazar_nodos(self):
        # Prueba de enlace entre nodos
        nodo1 = Nodo("valor 1")
        nodo2 = Nodo("valor 2")
        nodo1.nodo_siguiente = nodo2

        self.assertEqual(nodo1.nodo_siguiente, nodo2)
        self.assertIsNone(nodo2.nodo_siguiente)

    def test_repr_nodo(self):
        # Prueba de la representación en cadena del nodo
        nodo1 = Nodo("valor 1")
        nodo2 = Nodo("valor 2")
        nodo1.nodo_siguiente = nodo2

        self.assertEqual(str(nodo1), "Nodo(valor 1) -> Nodo(valor 2) -> None")
        self.assertEqual(str(nodo2), "Nodo(valor 2) -> None")

if __name__ == '__main__':
    unittest.main()