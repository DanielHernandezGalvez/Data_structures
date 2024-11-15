def arbol_binario(raiz):
    return [raiz, [], []]


def insertar_izquierda(raiz, nuevo_valor):
    rama_izquierda = raiz.pop(1)
    if len(rama_izquierda) > 1:
        raiz.insert(1, [nuevo_valor, rama_izquierda, []])
    else:
        raiz.insert(1, [nuevo_valor, [], []])
    
    return raiz

def insertar_derecha(raiz, nuevo_valor):
    rama_derecha = raiz.pop(2)
    if len(rama_derecha) > 1:
        raiz.insert(2, [nuevo_valor, [], rama_derecha])
    else:
        raiz.insert(2, [nuevo_valor, [], []])
    return raiz

def get_raiz(raiz):
    return raiz[0]

def set_raiz(raiz,valor):
    raiz[0] = valor

def get_hijo_izquierdo(raiz):
    return raiz[1]

def get_hijo_derecho(raiz):
    return raiz[2]

arbol = arbol_binario("A")

insertar_izquierda(arbol, "B")
insertar_derecha(arbol, "C")

insertar_izquierda(arbol, "D")
insertar_izquierda(arbol, "E")

insertar_derecha(arbol, "F")
insertar_derecha(arbol, "G")

print(arbol)

def imprimir_arbol(arbol, nivel=0, prefijo="Raíz: "):
    if arbol:
        print(" " * (nivel * 4) + prefijo + str(arbol[0]))
        if arbol[1]:
            imprimir_arbol(arbol[1], nivel + 1, "Izquierda: ")
        if arbol[2]:
            imprimir_arbol(arbol[2], nivel + 1, "Derecha: ")



# consultas

get_raiz(arbol)
set_raiz(arbol, "1")

print(get_hijo_izquierdo(arbol))

imprimir_arbol(arbol)