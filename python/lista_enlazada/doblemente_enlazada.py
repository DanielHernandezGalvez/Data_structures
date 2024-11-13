"""
"""

class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.nodo_siguiente = None
        self.nodo_anterior = None

nodo1 = Nodo("valor 1")
nodo2 = Nodo("valor 2")
nodo3 = Nodo("valor 3")

nodo1.nodo_siguiente = nodo2
nodo2.nodo_anterior= nodo1
nodo2.nodo_siguiente = nodo3
nodo3.nodo_anterior = nodo2

print(nodo2.nodo_siguiente.valor)