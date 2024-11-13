# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:20:38 2024

@author: Jerry
"""
import time
import random

def tamalitos(greñas):
    contador = 0
    running = True
    if not greñas:
        return 0
    while running:
        greñas.pop()
        contador += 1
        #if greñas is None:
        if not greñas:
            running = False
        return contador
    
def Bubble_Sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                #Intercambiar
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
                #print(f"Se intercambia {arr[j]} por {arr[j+1]}")
                #print(arr)
        #print(f"Fin de pasada: {i+1}")
    return arr

#ejemplo de uso
#arr = [5,3,8,4,2]
arr = [random.randint(1, 100) for i in range (1000)]
#Medir el tiempo de ejecucion
start_time = time.time()
print(Bubble_Sort(arr))
#Termina de ordenar el arreglo
end_time = time.time()
print(f"Ordenar {len(arr)} números: ")
print("Tiempo de ejecucion {:.6f} segundos".format(end_time-start_time))

