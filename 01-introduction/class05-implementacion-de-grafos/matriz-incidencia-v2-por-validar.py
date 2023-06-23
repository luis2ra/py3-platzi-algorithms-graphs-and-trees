'''
La matriz de adyacencia también se utiliza para representar grafos con algún peso, 
entonces si matriz[i][j] = p, entonces hay una relación del nodo i al nodo j con peso p.
'''

class MatrizIncidencia:
    def __init__(self, num_nodos, num_aristas):
        self.num_nodos = num_nodos
        self.num_aristas = num_aristas
        self.matriz = [[0] * num_aristas for _ in range(num_nodos)]

    def agregar_arista(self, nodo, arista):
        self.matriz[nodo][arista] = 1

    def imprimir_matriz(self):
        for fila in self.matriz:
            print(fila)

# Ejemplo de uso
grafo = MatrizIncidencia(4, 5)
grafo.agregar_arista(0, 0)
grafo.agregar_arista(0, 1)
grafo.agregar_arista(1, 1)
grafo.agregar_arista(2, 2)
grafo.imprimir_matriz()
