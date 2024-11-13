# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:09:16 2024

@author: Alumno
"""
import tkinter as tk
import random

#definir los colores RGB
colores_rgb = { 
                'Rojo': (255, 0, 0),
               'Verde': (0, 255, 0), 
               'Azul': (0, 137, 255),
               'Amarillo': (255, 255, 0)
               }
#Funcion para convertir RGB a Hx
def rgb_a_hex(rgb):
    return '#%02x%02x%02x' % rgb

class SimonDice:
    def __init__(self, ventana):
        #inicializar ña ventana y las variables del juego
        self.ventana = ventana
        self.ventana.title("Simon Dice")
        self.ventana.geometry("400x500")
        #lista de nombres de colores disponibles
        self.colores = list(colores_rgb.keys())
        #secuencia generada por el juego
        self.secuencia_juego = []
        #secuencia ingresada por el jugador
        self.secuencia_jugador = []
        #variable para controlar si se espera la entrada del jugador
        self.esperando_input = False
        #ronda actual
        self.ronda = 1
        #indice para controlar la recursion de la produccion de la secuencia
        self.indice_secuencia = 0
        #crear la interfaz grafica
        self.crear_interfaz()
    
    def crear_interfaz(self):
        #crear una etiqueta para mostrar la ronda actual
        self.label_ronda = tk.Label(self.ventana, text=f"Ronda{self.ronda}", font=('Arial', 20))
        self.label_ronda.pack(pady=20)
        #crear un boton que muestra los colores durante la secuencia
        self.boton_mostrar = tk.Button(self.ventana, bg='black', width=20, height=5, state ='disable')
        self.boton_mostrar.pack(pady=10)
        #crear un marco para los botones de colores
        self.frame_botones = tk.Frame(self.ventana)
        self.frame_botones.pack(pady=10)
        #crear los botones de colores para que el jugador ingrese la secuencia
        for color in self.colores:
            boton = tk.Button(self.frame_botones, text=color, bg=rgb_a_hex(colores_rgb[color]), width=10, height=3,command=lambda c=color:self.boton_clic(c))
            boton.pack(side='left', padx=5)
        #crear el boton para empezar el juego
        self.boton_empezar = tk.Button(self.ventana, text='Empezar juego', command=self.mostrar_secuencia)
        self.boton_empezar.pack(pady=20)
        
    def mostrar_secuencia(self):
        #inicializar variables para una nueva ronda
        self.esperando_input = False
        self.secuencia_jugador.clear()
        #añadir un nuevo color aleatorio a la secuencia del juego
        self.secuencia_juego.append(random.choice(self.colores))
        #actualizar la etiqueta de la ronda
        self.label_ronda.config(text=f"Ronda {self.ronda}")
        #desactivar el boton empezar
        self.boton_empezar.config(state='disabled')
        #inicializar la reproduccion de la secuencia desde el primer indice
        self.indice_secuencia = 0
        self.reproducir_secuencia()
        
    def reproducir_secuencia(self):
        #si aun hay colores en la secuencia por mostrar
        if self.indice_secuencia < len(self.secuencia_juego):
            #obtener el color actual
            color = self.secuencia_juego[self.indice_secuencia]
            #mostrar el color actual en el boton
            self.boton_mostrar.config(bg=rgb_a_hex(colores_rgb[color]))
            #esperar 1 segundo antes de apagar el color
            self.ventana.after(1000, self.apagar_color)
        else:
            #si se ha mostrado toda la secuencia, iniciar el turno del jugador
            self.boton_mostrar.config(bg='black')
            self.iniciar_input_jugador()
            
    def apagar_color(self):
        #apagar el color(volver el boton a color gris)
        self.boton_mostrar.config(bg='black')
        #incrementar el indice para pasar al siguiente color
        self.indice_secuencia +=1
        #esperar 0.5 segundos antes de mostrar el siguiente color
        self.ventana.after(500, self.reproducir_secuencia)
        
    def iniciar_input_jugador(self):
        #indicar que ahora se espera la entrada del jugador
        self.esperando_input = True
        #mostrar mensaje al jugador
        tk.messagebox.showinfo("Tu turno", "Ahora es tu turno de repetir la secuencia")
        
    def boton_clic(self, nombre_color):
        #si se esta esperando la entrada del jugador
        if self.esperando_input:
            #añadir el color seleccionado por el jugador a su secuencia
            self.secuencia_jugador.append(nombre_color)
            #obtener el indice actual
            indice_actual = len(self.secuencia_jugador) - 1
            #verificar si el ultimo color ingresado es correcto
            if self.secuencia_jugador[indice_actual] != self.secuencia_juego[indice_actual]:
                #si es incorrecto,  mostrar mensaje y reiniciar el juego
                tk.messagebox.showerror("Error", "¡Incorrecto! hasta aqui llegaste")
                self.reiniciar_juego()
            elif len(self.secuencia_jugador) == len(self.secuencia_juego):
                #si la secuencia esta completa y es correcta, avanzar a la siguiente ronda
                self.ronda += 1
                tk.messagebox.showinfo("Correcto", "¡Correcto! avanza a la siguiente ronda")
                #esperar 1 segundo antes de iniciar la siguiente ronda
                self.ventana.after(1000, self.mostrar_secuencia)
                
    def reiniciar_juego(self):
        #reiniciar las variables del juego
        self.secuencia_juego.clear()
        self.secuencia_jugador.clear()
        self.ronda = 1
        #activar el boton de empezar
        self.boton_empezar.config(state='normal')
        #actualizar la etiqueta de la ronda
        self.label_ronda.config(text = f"Ronda{self.ronda}")
        
if __name__ == "__main__":
    #crear la ventana principal de tkinter
    ventana = tk.Tk()
    #crear una instancia del juego
    juego = SimonDice(ventana)
    #iniciar el bucle principal de la ventana
    ventana.mainloop()
                
        