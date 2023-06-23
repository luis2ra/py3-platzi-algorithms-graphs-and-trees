# desarrollada con otro arbol binario
'''
Solución iterativa:

Primero se insertan todos los elementos en la pila y luego se hace uso de la cabeza de la 
pila (que es el último nodo insertado), así que el primer nodo que se maneja es el último hijo.

'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def dfs(raiz, objetivo):
    counter = 0
    if raiz is None:
        return None

    pila = []
    pila.append(raiz)

    while pila:
        counter += 1
        nodo_actual = pila.pop()

        # Comprobar si el nodo actual contiene el elemento buscado
        if nodo_actual.valor == objetivo:
            print("conteo de busquedas: ", counter)
            return nodo_actual

        # Agregar el hijo derecho y luego el hijo izquierdo a la pila
        if nodo_actual.derecha:
            pila.append(nodo_actual.derecha)
        if nodo_actual.izquierda:
            pila.append(nodo_actual.izquierda)

    print("conteo de busquedas: ", counter)
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
