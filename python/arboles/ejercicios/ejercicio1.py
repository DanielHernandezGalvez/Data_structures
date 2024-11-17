"""
dado un arbol binario, verificar si es un arbol de búsqueda binaria o no
un arbol de busqueda binaria debe cumplir con estas 3 condiciones:
1- todos los valores de los nodos del subarbol izquiedo son menores
    que el valor del nodo raiz
2- todos los valores de los nodos del subarbol derecho son mayores que
    el valor del nodo raiz
3- todos los subarboles deben ser también arboles de busqueda binaria
"""

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
        
# valores_arbol = []

def recorrer_inorder(arbol):
    if arbol:
        recorrer_inorder(arbol.get_izquierdo())
        valores_arbol.append(arbol.get_raiz())
        recorrer_inorder(arbol.get_derecho())
        
def verificar_ordenados(valores_arbol):
    return valores_arbol == sorted(valores_arbol)

arbol = Arbol_binario(8)
arbol.insertar_izquierda(3)
arbol.insertar_derecha(10)
arbol.insertar_izquierda(1)
arbol.insertar_derecha(2)

valores_arbol = []
recorrer_inorder(arbol)
print(valores_arbol)

resultado = (verificar_ordenados(valores_arbol))
print(resultado)
