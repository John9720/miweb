#GUI = Graphical User Interface
#Tkinter = TK Interface
import tkinter as tk
from tkinter import ttk, messagebox, Menu
import sys
from tkinter.ttk import *
import sticky

'''
ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Hola Mundo")
#Creamos un boton (widget), el objeto padre es la ventana
def evento_click():
    boton1.config(text="Botón presionado")
    print("Ejecución del evento")
    #creamos un nuevo botón
    boton2 = ttk.Button(ventana, text="Nuevo botón")
    boton2.pack()
boton1 = ttk.Button(ventana, text="Dar click", command=evento_click)
#Usar pack layout manager para mostrar el boton
boton1.pack()
#Inicamos la ventana (se debe ejecutar hasta el final)
ventana.mainloop()
'''

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Manejo de Componentes")



entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)
#entrada1.insert(0, "Ingresa una cadena")
#entrada1.insert(tk.END, ".")
#entrada1.config(state="readonly")

etiqueta1 = tk.Label(ventana, text="Aqui se mostrará el contenido de la caja de texto")
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
    etiqueta1.config(text=entrada1.get())
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo("Mensaje Informativo", mensaje1 + " Informativo")

def salir():
    ventana.quit()
    ventana.destroy()
    print("Salimos de la aplicación")
    sys.exit()

def crear_menu():
    #configurar el menú principal
    menu_principal = Menu(ventana)
    #tearoff = False para evitar que se separe de la interfaz
    submenu_archivo = Menu(menu_principal, tearoff=False)
    submenu_archivo.add_command(label="Nuevo")
    submenu_archivo.add_command(label="Salir", command=salir)
    menu_principal.add_cascade(menu=submenu_archivo, label="Archivo")
    submenu_ayuda = Menu(menu_principal, tearoff=False)
    submenu_ayuda.add_command(label="Acerca De")
    menu_principal.add_cascade(menu=submenu_ayuda, label="Ayuda")
    ventana.config(menu=menu_principal)

#Creamos botón
boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.grid(row=0, column=1)

crear_menu()

ventana.mainloop()