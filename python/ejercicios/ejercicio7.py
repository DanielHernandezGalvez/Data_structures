"""
Construir una clase Duplicados y su función contiene_duplicados
dado un array de numeros, devuelve True si hay duplicados, False en caso contrario
d = Duplicados()
d.contiene_duplicados([1,2,3,4,1]) --> True
d.contiene_duplicados([1,2,3,4]) --> False
"""

class Duplicados:
    def contiene_duplicados(self,numeros):
        conjunto = set() 

        for num in numeros:
            if num in conjunto:
                return True
            else:
                conjunto.add(num)
            
        return False
    
d = Duplicados()
print(d.contiene_duplicados([1,2,3,4]))

        