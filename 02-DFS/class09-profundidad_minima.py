'''
Calculo de la profundidad de un arbol

'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def profundidad_minima(raiz):
    if not raiz:
        return 0

    izquierda = profundidad_minima(raiz.izquierda)
    derecha = profundidad_minima(raiz.derecha)
    if not izquierda:
        return derecha + 1
    elif not derecha:
        return izquierda + 1
    else:
        return min(izquierda, derecha) + 1


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

# Profundidad de un arbol
print(profundidad_minima(raiz))
