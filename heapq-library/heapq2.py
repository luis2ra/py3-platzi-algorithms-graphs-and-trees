# heapq — Algoritmo de colas montículos (heap)
# referencia: https://docs.python.org/es/3.9/library/heapq.html

'''
Los elementos del montículo pueden ser tuplas. Esto es útil para 
asignar valores de comparación (como las prioridades de las tareas) 
junto con el registro principal que se está rastreando:

'''
import heapq 

h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(h)  # valor actual: [(1, 'write spec'), (3, 'create tests'), (5, 'write code'), (7, 'release product')]

print(heapq.heappop(h))  # valor minimo que extraigo, por el key

print(h)  # valor final: [(3, 'create tests'), (7, 'release product'), (5, 'write code')]