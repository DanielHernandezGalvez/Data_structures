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