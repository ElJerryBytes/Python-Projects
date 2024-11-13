# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:20:44 2024

@author: Jerry
"""

import time 
#factorial sin recursividad 
def factorial_1(n):
    tamal = 1
    for i in range(2, n+1):
        tamal = tamal * 1
        return tamal 
    #ejemplo de uso 
    numerito = 10000
    inicio = time.time()
    print(f"El factroial de{numerito}es{factorial_1(numerito)}")
    fin = time.time()
    print(f"El tiempo de ejecucion es: {fin - inicio} s")
    
    
    #factorial con recursividad 
    def factorial_2(n):
        if n == 0 or n == 1 :
            return 1
        else:
            return n * factorial_2(n-1)
    #ejemplo de uso 
    numerito = 100
    inicio = time.time()
    print(f"El factroial de{numerito}es{factorial_1(numerito)}")
    fin = time.time()
    print(f"El tiempo de ejecucion es: {fin - inicio} s")