"""
Pilas
LIFO: ultimo en entrar primero en salir
ejemplo una pila de libros, el ultimo que pones es el primero que puedes quitar
"""

class Pila():
    def __init__(self):
        self.elementos = []
    
    def esta_vacia(self):
        return self.elementos == []
    
    def insertar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self):
        return self.elementos.pop()
    
    def consultar(self):
        return self.elementos[len(self.elementos) - 1]
    
    def longitud(self):
        return len(self.elementos)
    
p = Pila()
p.insertar("libro verde")
p.insertar("libro azul")
p.insertar("libro rojo")

p.longitud()

print(p.longitud())
print(p.eliminar())
print(p.consultar())