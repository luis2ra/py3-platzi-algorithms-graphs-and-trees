# desarrollada con un arbol binario
'''
Solución recursiva:

En este ejemplo, el algoritmo DFS recursivo utiliza llamadas recursivas para explorar los 
nodos del árbol. Comienza verificando si el nodo actual contiene el elemento buscado. Si es 
así, se devuelve el nodo. Si no, se realiza una llamada recursiva al subárbol izquierdo y se 
verifica si se encuentra el elemento allí. Si se encuentra, se devuelve el nodo encontrado. Si 
no, se realiza una llamada recursiva al subárbol derecho y se verifica si se encuentra el 
elemento allí. Si se encuentra, se devuelve el nodo encontrado. Si no se encuentra el 
elemento en todo el árbol, el algoritmo devuelve None.

'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def dfs(raiz, objetivo):
    if raiz is None:
        return None

    # Comprobar si el nodo actual contiene el elemento buscado
    if raiz.valor == objetivo:
        return raiz

    # Recorrer el subárbol izquierdo de forma recursiva
    nodo_encontrado = dfs(raiz.izquierda, objetivo)
    if nodo_encontrado:
        return nodo_encontrado

    # Recorrer el subárbol derecho de forma recursiva
    nodo_encontrado = dfs(raiz.derecha, objetivo)
    if nodo_encontrado:
        return nodo_encontrado

    # Si no se encuentra el elemento en el árbol
    return None


# Crear un árbol binario de ejemplo
raiz = Nodo(25)

# Nivel 1
raiz.izquierda = Nodo(10)
raiz.derecha = Nodo(40)

# Nivel 2
raiz.izquierda.izquierda = Nodo(8)
raiz.izquierda.derecha = Nodo(13)

raiz.derecha.izquierda = Nodo(30)
raiz.derecha.derecha = Nodo(42)

# Nivel 3
raiz.izquierda.izquierda.izquierda = Nodo(6)
raiz.izquierda.derecha.derecha = Nodo(15)
raiz.derecha.izquierda.izquierda = Nodo(26)
raiz.derecha.derecha.derecha = Nodo(49)

# Nivel 4
raiz.izquierda.izquierda.izquierda.izquierda = Nodo(1)
raiz.izquierda.izquierda.izquierda.derecha = Nodo(7)
raiz.derecha.derecha.derecha.izquierda = Nodo(45)
raiz.derecha.derecha.derecha.derecha = Nodo(51)

# Ejemplo de búsqueda de un elemento en el árbol usando DFS iterativo
elemento_buscado = 30
nodo_encontrado = dfs(raiz, elemento_buscado)

if nodo_encontrado:
    print("Se encontró el elemento", elemento_buscado)
else:
    print("No se encontró el elemento", elemento_buscado)
