# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:21:36 2024

@author: Jerry
"""

import time 
#fabonacci 
def fibonacci_1(n):
    if n  == 0:
        return 0
    elif n == 1 :
        return 1 
    else:
        return fibonacci_1(n-1) + fibonacci_1(n-2)
    
#ejemplo de uso 
    numerito = 50
    inicio = time.time()
    print(f"La serie de fibonacci hasta {numerito}numero es{factorial_1(numerito)}")
    fin = time.time()
    print(f"El tiempo de ejecucion es: {fin - inicio} s"