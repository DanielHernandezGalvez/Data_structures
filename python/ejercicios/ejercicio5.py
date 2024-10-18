"""
Dadas 2 listas, encontrar los elementos que están en una lista y no están en la otra lista
buscar([1,2,3,4,5,6], [6,3,2,3]) --> [1,5]
buscar([1,2,3,"hola"], [2,3]) --> [1,"hola"]
"""

def buscar(lista1,lista2):
    return [elemento for elemento in lista1 if elemento not in lista2]  




print(buscar([1,2,3,"hola"], [2,3]))