"""
Crear una clase que implemente la estructura de datos de
una cola, utilizando 2 pilas, una cola mantiene el orden de los 
elementos (el primero en entrar, es el primero en salir)
una pila cambia el orden de los elementos (el ultimo en entrar es el primero en salir)
"""

class Cola():
    def __init__(self):
        self.entrada = []
        self.salida = []

    def insertar(self, elemento):
        self.entrada.append(elemento)

    def eliminar(self):
        if not self.salida:
            while self.entrada:
                self.salida.append(self.entrada.pop())
        return self.salida.pop()

c = Cola()

c.insertar(10)
c.insertar(2)
c.eliminar()

print(c.salida) # [10, 2]  # 2