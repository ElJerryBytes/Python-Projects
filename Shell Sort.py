# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:37:47 2024

@author: Jerry
"""
import time
import random

def Shell_Sort(arr):
    #Inicializar el tamaño de la lista
    n = len(arr)
    #Empezar con el intervalo igual a la mitad del tamaño de la lista
    gap = int(n/2) #gap es entero, n//2 (para hacerlo entero)
    #Continuar reduciendo el intervalo hastallegar a 0
    while gap > 0:
        #Recorrer la lista desde el indice igual al intevalo o gap hasta el final
        for i in range(gap, n):
            #Guardar el valor actual en una variable temporal
            temp = arr[i]
            #Inicializar la variable j en la posición i
            j = i
            #Desplazar los elementos del subarreglo ordenado si son mayores que el valor temporal
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            #Insertar el valor temporal en la posición correcta
            arr[j] = temp
            #Ver las listas temporales
            #print(arr)
        #Reducir el gap
        gap = int(gap/2)
    return arr

'''
#Ejemplo de uso
arr=[8,6,7,2,1,4,5,3]
#arr = [random.randint(1,100) for i in range(1000)]
#Medir el tiempo de ejecución
start_time = time.time()
print(Shell_Sort(arr))
#Termina de ordenar el arreglo
end_time = time.time()
print(f"Ordenar {len(arr)} números:")
print("Tiempo de ejecución: {:.6f} segundos".format(end_time - start_time))
'''
