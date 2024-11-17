"""
Imprimir un arbol bionario por niveles
en cada linea mostrar una lista con los elementos de ese nivel del arbol
"""

class Nodo:
    def __init__(self, value):
        self.valor = value
        self.izquierdo = None
        self.derecho = None
        
import collections

def imprimir_nivel(arbol):
    if arbol:
        nodos = collections.deque([arbol])
        contador = 1
        proximo = 0
        
        valores = []
        while len(nodos) != 0:
            nodo = nodos.popleft()
            contador -= 1
            
            valores.append(nodo.valor)
            
            if nodo.izquierdo:
                nodos.append(nodo.izquierdo)
                proximo += 1
            
            if nodo.derecho:
                nodos.append(nodo.derecho)
                proximo += 1
                
            if contador == 0:
                print(valores)
                contador = proximo
                proximo = 0
                valores = []

arbol = Nodo(8)
arbol.izquierdo = Nodo(3)
arbol.derecho = Nodo(10)

print(imprimir_nivel(arbol))
