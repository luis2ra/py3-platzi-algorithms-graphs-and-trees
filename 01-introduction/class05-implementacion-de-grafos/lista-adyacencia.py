class ListaAdyacencia:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.lista = [[] for _ in range(num_nodos)]

    def agregar_arista(self, nodo_origen, nodo_destino):
        self.lista[nodo_origen].append(nodo_destino)

    def imprimir_lista(self):
        for nodo, adyacentes in enumerate(self.lista):
            print(f"Nodo {nodo}: {adyacentes}")

# Ejemplo de uso
grafo = ListaAdyacencia(4)
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)

# print(grafo.num_nodos)
# print(grafo.lista[0])
grafo.imprimir_lista()