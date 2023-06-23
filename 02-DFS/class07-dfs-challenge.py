'''
Usando la referencia grafica del arbol en el archivo "class07-dfs-challenge.png",
buscar el valor de nodo/vertice con valor 30

'''

class lista_adyacencia:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.lista = [[] for _ in range(num_nodos)]

    def agregar_arista(self, nodo_origen, nodo_destino):
        self.lista[nodo_origen].append(nodo_destino)

    def imprimir_lista(self):
        for nodo, adyacentes in enumerate(self.lista):
            print(f"Nodo {nodo}: {adyacentes}")



# Ejemplo de uso
grafo = lista_adyacencia(15)

# Nodo raiz
grafo.agregar_arista(25, 10)
grafo.agregar_arista(25, 40)

# # Nivel 1
# grafo.agregar_arista(10, 8)
# grafo.agregar_arista(10, 13)
# grafo.agregar_arista(40, 30)
# grafo.agregar_arista(40, 42)

# # Nivel 2
# grafo.agregar_arista(8, 6)
# grafo.agregar_arista(13, 15)
# grafo.agregar_arista(30, 26)
# grafo.agregar_arista(42, 49)

# # Nivel 3
# grafo.agregar_arista(6, 1)
# grafo.agregar_arista(6, 7)
# grafo.agregar_arista(49, 45)
# grafo.agregar_arista(49, 51)

print(grafo.num_nodos)
print(grafo.lista)
# grafo.imprimir_lista()