# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:14:22 2024

@author: Jerry
"""

class Cola:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        #verificar que la cola esta vacia
        return len(self.items) == 0
    
    def encolar(self, item):
        #agregar un elemento al rear de la cola
        self.items.append(item)
        
    def desencolar(self):
        #eliminamos el elemento frontal
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items.pop(0)
    
    def size(self):
        #obtener el tamaño de la cola
        return len(self.items)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items[0]

class Paciente:
    def __init__(self, nombre, hora_llegada):
        self.nombre = nombre
        self.hora_llegada = hora_llegada
        
def main():
    queue = Cola()
    print("Bienvenido al sistema")
    while True:
        print("Opciones: ")
        print("1. Agregar paciente")
        print("2. Atender al siguiente paciente")
        print("3. Ver el siguiente paciente")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del paciente: ")
            hora_llegada = input("Introduce la hora de llegada (ejemplo 10:00 am): ")
            paciente = Paciente(nombre, hora_llegada)
            queue.encolar(paciente)
            print(f"Paciente {nombre} añadido a la cola\n")
            
        elif opcion == "2":
            if not queue.is_empty():
                paciente = queue.desencolar()
                print(f"Paciente {paciente.nombre} atendido\n")
            else:
                print("La cola está vacía\n")
                
        elif opcion == "3":
            if not queue.is_empty():
                paciente = queue.peek()
                print(f"Siguiente paciente en atender: {paciente.nombre}, Hora de llegada: {paciente.hora_llegada}\n")
            else:
                print("Ya no hay pacientes\n")
                
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida")
            
if __name__ == "__main__":
    main()
