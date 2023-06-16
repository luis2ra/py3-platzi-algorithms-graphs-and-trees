# heapq — Algoritmo de colas montículos (heap)
# referencia: https://docs.python.org/es/3.9/library/heapq.html

'''
Un "heapsort" puede ser implementado empujando todos los valores en un 
montículo y luego desapilando los valores más pequeños uno a la vez:

'''
import heapq 

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(heapsort(data))

data = [11, 3, 15, 7, 19, 2, 14, 6, 8, 0]
print(heapsort(data))
