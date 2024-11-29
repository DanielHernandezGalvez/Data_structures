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
        
arbol = Arbol_binario("a")
arbol.get_raiz()
arbol.insertar_izquierda("b2")
arbol.insertar_izquierda("b")
arbol.insertar_derecha("c2")
arbol.insertar_derecha("c")
# print(arbol.get_izquierdo().valor)

# RECORRER EL ARBOL preorder, inorder, postorder

# PREORDER raiz en primera posicion

def preorder(arbol):
    if arbol:
        print(arbol.get_raiz())
        preorder(arbol.get_izquierdo())
        preorder(arbol.get_derecho())
        
# print(preorder(arbol))

# INORDER la raiz va en el centro

def inorder(arbol):
    if arbol:
        inorder(arbol.get_izquierdo())
        print(arbol.get_raiz())
        inorder(arbol.get_derecho())
        
# print(inorder(arbol))

# POSTORDER raiz en ultima posicion

def post_order(arbol):
    if arbol != None:
        post_order(arbol.get_izquierdo())
        post_order(arbol.get_derecho())
        print(arbol.get_raiz())
        
print(post_order(arbol))