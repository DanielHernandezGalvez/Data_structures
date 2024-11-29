"""
Estructura FIFO: primero en entrar, primero en salir
cola de personas esperando el autobus, el primero en la cola sera el pormero en subir
"""

class Cola():
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
            return self.elementos == []
        
    def insertar(self, elemento):
            self.elementos.insert(0,elemento)

    def eliminar(self):
            return self.elementos.pop()

    def longitud(self):
            return len(self.elementos)
        
c = Cola()
c.insertar(1)
c.insertar(2)
c.insertar(3)
print(c.longitud())