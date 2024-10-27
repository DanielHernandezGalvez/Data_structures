"""
Dada una lista de parentesis, corchetes y llaves pasados como parámetro
a la función "balanceados", devolver True si los elementos estan balanceados o 
False en caso contrario.
Tipos de parentesis (), [], {}
ejemplo balanceado ([]), (){}
ejemplo no balanceado ([)]
Pista: utilizar pilas para ir almacenando los elementos (parentesis, corchetes y llaves)
balanceados ('[]') --> True
balanceados ('[](){}') --> True
balanceados ('[()]') --> True
balanceados ('[](') --> True
"""

def balanceados(cadena):
    if len(cadena) % 2 != 0:
        return False
    
    abiertos = set("({[")
    emparejamientos = set([ ( '(', ')' ), ( '[', ']' ), ( '{', '}' ), ])
    
    pila = []
    
    for elemento in cadena:
        if elemento in abiertos:
            pila.append(elemento)
        else:
            if len(cadena) == 0:
                return False
            
            anterior = pila.pop()
            if (anterior, elemento) not in emparejamientos:
                return False
            
    return len(pila) == 0

print(balanceados ('[]('))