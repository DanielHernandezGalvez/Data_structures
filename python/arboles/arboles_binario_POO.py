class Arbol_binario():
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        
    def insertar_izquierda(self, Nodo):
        if self.izquierdo == None:
            self.izquierdo = Arbol_binario(Nodo)
        else:
            arbol = Arbol_binario(Nodo)
            arbol.izquierdo = self.izquierdo
            self.izquierdo = arbol
            
    def insertar_derecha(self, Nodo):
        if self.derecho == None:
            self.derecho = Arbol_binario(Nodo)
        else:
            arbol = Arbol_binario(Nodo)
            arbol.derecho = self.derecho
            self.derecho = arbol
            
    def get_raiz(self):
        return self.valor
    
    def get_izquierdo(self):
        return self.izquierdo
    
    def get_derecho(self):
        return self.derecho
    
    def set_raiz(self,nuevo_valor):
        self.valor = nuevo_valor
        
a = Arbol_binario("a")
a.get_raiz()
a.insertar_derecha("c")
a.insertar_izquierda("b")
print(a.get_izquierdo().valor)
