class ListaIncidencia:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.lista = [[] for _ in range(num_nodos)]

    def agregar_arista(self, nodo_origen, nodo_destino, peso=None):
        arista = {"destino": nodo_destino, "peso": peso}
        self.lista[nodo_origen].append(arista)

    def imprimir_lista(self):
        for nodo, aristas in enumerate(self.lista):
            print(f"Nodo {nodo}: {aristas}")


# Ejemplo de uso
grafo = ListaIncidencia(4)
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3, 5)
grafo.imprimir_lista()
