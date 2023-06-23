'''
En matemáticas, la sucesión de Fibonacci es la siguiente sucesión infinita de números naturales:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, ...

Ahora, viendo la sucesión por el número de de elementos:
n = 0 => 1
n = 1 => 1
n = 2 => 2
n = 3 => 3
n = 4 => 5 
n = 5 => 8
n = 6 => 13
n = 7 => 21

'''

def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return fibo(n-1) + fibo(n-2)
    else:
        return 'Valor de "n" inválido'
    

number = int(input('Valor "n" para calcular la serie: '))
print(fibo(number))
