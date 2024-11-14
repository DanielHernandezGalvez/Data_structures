"""
Construir la funcion circular que tomando como parametro un nodo, 
verifique si pertenece a una lista circular
construir una lista circular y otra lista no circular para 
realizar pruebas
crear tambien una clase de test para probar la funcón ciruclar
Ejemplo:
(nodo1 -> nodo2 -> nodo3 -> nodo1) ---> True
(nodo1 -> nodo2 -> nodo3 -> nodo4) ---> False
"""

def circular(nodo):
    marcador1 = nodo
    marcador2 = nodo
    
    while marcador2 != None and marcador2.nodo_siguiente != None:
        marcador1 = marcador1.nodo_siguiente
        marcador2 = marcador2.nodo_siguiente.nodo_siguiente
        if marcador1 == marcador2:
            return True
        
    return False

class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.nodo_siguiente = None
        
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)

nodo1.nodo_siguiente = nodo2
nodo2.nodo_siguiente = nodo3
nodo3.nodo_siguiente = nodo1

nodo5 = Nodo(5)
nodo6 = Nodo(6)

nodo5.nodo_siguiente = nodo6

print(circular(nodo5))
