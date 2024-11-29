# lista = [1,2,4,5,6,7,8,9,12,14]
# busqueda_binaria_recursiva(lista,2) -- True
# busqueda_binaria_recursiva(lista,3) -- False

def busqueda_binaria_recursiva(lista, elemento):
    if len(lista) == 0:
        return False
    else:
        medio = len(lista) // 2
        if lista[medio] == elemento:
            return True
        else:
            if elemento < lista[medio]:
                return busqueda_binaria_recursiva(lista[:medio], elemento)
            else:
                return busqueda_binaria_recursiva(lista[medio + 1:], elemento)

lista = [1,2,4,5,6,7,8,9,12,14]

print(busqueda_binaria_recursiva(lista, 15))
