'''
La matriz de adyacencia es una matriz 2D de tamaño n x n donde n es el número de nodos de un grafo. 
Sea la matriz 2D matriz[][], una casilla matriz[i][j] = 1 indica que hay una relación del nodo i al nodo j.

'''
class MatrizAdyacencia:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.matriz = [[0] * num_nodos for _ in range(num_nodos)]

    def agregar_arista(self, nodo_origen, nodo_destino):
        self.matriz[nodo_origen][nodo_destino] = 1
        self.matriz[nodo_destino][nodo_origen] = 1

    def imprimir_matriz(self):
        for fila in self.matriz:
            print(fila)

# Ejemplo de uso
grafo = MatrizAdyacencia(4)
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)
grafo.imprimir_matriz()
