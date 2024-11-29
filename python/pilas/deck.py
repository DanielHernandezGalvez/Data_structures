"""
mezcla entre una pila y una cola
se pueden insertar al principio o al final
se pueden eliminar del principio o del final
"""

class Deque():
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return self.elementos == []
    
    def insertar(self, elemento):
        self.elementos.append(elemento)

    def insertar_cola(self, elemento):
        self.elementos.insert(0,elemento)

    def eliminar_cabeza(self):
        return self.elementos.pop()
    
    def eliminar_cola(self):
        return self.elementos.pop(0)
    
    def longitud(self):
        return len(self.elementos)
    
d = Deque()
d.insertar(1)
d.insertar(2)

print(d.longitud()) # 2