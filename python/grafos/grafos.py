class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conexiones = {}

    def incluir_vecino(self, vecino, peso):
        self.conexiones[vecino] = peso

    def ver_conexiones(self):
        return self.conexiones.keys()

    def ver_id(self):
        return self.id

    def ver_peso(self, vecino):
        return self.conexiones[vecino]

    def __str__(self):
        return str(self.id) + " conectado con " + str([x for x in self.ver_conexiones()])


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def incluir_vertice(self, clave):
        nuevo_vertice = Vertice(clave)
        self.vertices[clave] = nuevo_vertice
        self.num_vertices += 1
        return nuevo_vertice

    def ver_vertice(self, clave):
        return self.vertices.get(clave, None)

    def incluir_arista(self, origen, destino, peso=0):
        if origen not in self.vertices:
            self.incluir_vertice(origen)
        if destino not in self.vertices:
            self.incluir_vertice(destino)

        self.ver_vertice(origen).incluir_vecino(destino, peso)

    def ver_lista_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())


# Uso del grafo
grafo = Grafo()
grafo.incluir_vertice(1)
grafo.incluir_vertice(2)
grafo.incluir_vertice(3)
grafo.incluir_vertice(4)

grafo.incluir_arista(1, 2, 4)
grafo.incluir_arista(1, 4, 2)
grafo.incluir_arista(2, 4, 1)
grafo.incluir_arista(2, 3, 1)

print("Vértices en el grafo:", grafo.ver_lista_vertices())

for vertice in grafo:
    print(vertice)