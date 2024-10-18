"""
Dada una lista de números positivos y negaticos, encontrar la suma continua de mayor valor
ejemplo, maximo_suma_continua([4,8,6,-3,2,-4,1,-1]) --> 18
"""
def maximo_suma_continua(lista):

    if len(lista) == 0:
        return 0
    
    maximo = suma = lista[0]

    for numero in lista[1:]:
        suma = max(numero + suma, numero)
        maximo = max(maximo, suma)
    
    return maximo

 
# print( maximo_suma_continua([4,8,6,-3,2,-4,1,-1]))

# Clase de prueba de la funcionanterior "maximo_suma_continua"

from nose.tools import assert_equal

class Probas_maximo_suma_continua(object):
    def prueba1(self):
        assert_equal(maximo_suma_continua([4,8,6,-3,2,-4,1,-1]), 18)
        assert_equal(maximo_suma_continua([1,5,-2,4,-3,2]), 8)
        print("Todos las pruebas se han ejecutado correctamente")

print( maximo_suma_continua([1,5,-2,4,-3,2]))

prueba = Probas_maximo_suma_continua()
prueba.prueba1()
