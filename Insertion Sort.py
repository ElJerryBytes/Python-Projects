# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:32:05 2024

@author: Jerry
"""
import time
import random

def Insertion_Sort(arr):
    n = len(arr)
    for i in range(1,n):
        aux = arr[i]
        j = i -1
        while j >= 0 and aux < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = aux
    return arr

#ejemplo de uso
#arr = [5,3,8,4,2]
arr = [random.randint(1, 100) for i in range (10)]
#Medir el tiempo de ejecucion
start_time = time.time()
print(Insertion_Sort(arr))
#Termina de ordenar el arreglo
end_time = time.time()
print(f"Ordenar {len(arr)} números: ")
print("Tiempo de ejecucion {:.6f} segundos".format(end_time-start_time))