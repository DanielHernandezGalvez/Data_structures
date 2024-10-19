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

from nose.tools import assert_equal

class TestDuplicados:
    
    def test_con_duplicados(self):
        d = Duplicados()
        assert_equal(d.contiene_duplicados([1, 2, 3, 4, 1]), True)
        assert_equal(d.contiene_duplicados([5, 5, 5, 5]), True)
    
    def test_sin_duplicados(self):
        d = Duplicados()
        assert_equal(d.contiene_duplicados([1, 2, 3, 4]), False)
        assert_equal(d.contiene_duplicados([7, 8, 9]), False)
    
    def test_lista_vacia(self):
        d = Duplicados()
        assert_equal(d.contiene_duplicados([]), False)
    
    def test_un_solo_elemento(self):
        d = Duplicados()
        assert_equal(d.contiene_duplicados([1]), False)

        print(d.contiene_duplicados([1,2,3,4]))

# Ejecutar los tests
if __name__ == '__main__':
    t = TestDuplicados()
    t.test_con_duplicados()
    t.test_sin_duplicados()
    t.test_lista_vacia()
    t.test_un_solo_elemento()

    print("Todos los tests pasaron correctamente.")