"""
Funcion dentro de una clas
inprime los indices de cada par de números que sumen el valor "suma" pasado como parámetro
s.suma_2_elementos([2,3,4], 3) --> [0,1]
s.suma_2_elementos([11,2,3,4,5,6,2], 4) --> [0,2]  [1,6]
mejora: devolver una lista en lugar de imprimir el resultado
"""

class Solucion:
    def suma_2_elementos(self, numeros, suma):
        diccionario = {} # valor: indice  1:0

        for indice, numero in enumerate(numeros):
            diferencia = suma - numero
            if diferencia in diccionario:
                print([diccionario[diferencia], indice])
            diccionario[numero] = indice
        return

s = Solucion()
s.suma_2_elementos([11,2,3,4,5,6,2], 4)