'''
La matriz de adyacencia también se utiliza para representar grafos con algún peso, 
entonces si matriz[i][j] = p, entonces hay una relación del nodo i al nodo j con peso p.

'''
class MatrizIncidencia:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.matriz = [[0] * num_nodos for _ in range(num_nodos)]

    def agregar_arista(self, nodo_origen, nodo_destino, peso = 1):
        self.matriz[nodo_origen][nodo_destino] = peso
        self.matriz[nodo_destino][nodo_origen] = peso

    def imprimir_matriz(self):
        for fila in self.matriz:
            print(fila)

# Ejemplo de uso
grafo = MatrizIncidencia(4)
grafo.agregar_arista(0, 1, 2)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2, 3)
grafo.agregar_arista(2, 3)
grafo.imprimir_matriz()
