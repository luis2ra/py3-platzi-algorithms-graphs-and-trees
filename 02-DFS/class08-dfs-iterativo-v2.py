# desarrollada con un arbol binario
'''
En este ejemplo, el algoritmo DFS iterativo utiliza una pila para rastrear los nodos del árbol.
Comienza por agregar la raíz a la pila y luego itera hasta que la pila esté vacía. En cada 
iteración, se toma el nodo superior de la pila y se verifica si contiene el elemento buscado. Si 
es así, se devuelve el nodo. Luego, se agregan los hijos derecho e izquierdo del nodo actual a 
la pila (en ese orden) si existen. Si no se encuentra el elemento en todo el árbol, el 
algoritmo devuelve None.

Primero se insertan todos los elementos en la pila y luego se hace uso de la cabeza de la 
pila (que es el último nodo insertado), así que el primer nodo que se maneja es el último hijo.

'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def dfs(raiz, objetivo):
    if raiz is None:
        return None

    pila = []
    pila.append(raiz)

    while pila:
        nodo_actual = pila.pop()

        # Comprobar si el nodo actual contiene el elemento buscado
        if nodo_actual.valor == objetivo:
            return nodo_actual

        # Agregar el hijo derecho y luego el hijo izquierdo a la pila
        if nodo_actual.derecha:
            pila.append(nodo_actual.derecha)
        if nodo_actual.izquierda:
            pila.append(nodo_actual.izquierda)

    # Si no se encuentra el elemento en el árbol
    return None


# Crear un árbol binario de ejemplo
raiz = Nodo(10)
raiz.izquierda = Nodo(7)
raiz.derecha = Nodo(15)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(9)
raiz.derecha.izquierda = Nodo(12)
raiz.derecha.derecha = Nodo(20)

# Ejemplo de búsqueda de un elemento en el árbol usando DFS iterativo
elemento_buscado = 12
nodo_encontrado = dfs(raiz, elemento_buscado)

if nodo_encontrado:
    print("Se encontró el elemento", elemento_buscado)
else:
    print("No se encontró el elemento", elemento_buscado)
