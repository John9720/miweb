#GUI = Graphical User Interface
#Tkinter = TK Interface
import tkinter as tk
from tkinter import ttk, messagebox, Menu, scrolledtext
import sys
from tkinter.ttk import *
import sticky
from time import sleep

class ComponentesVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("650x400+650+250")
        self.title("Componentes")
        self._crear_tabs()

    def _crear_componentes_tabulador1(self, tabulador):
        etiqueta1 = ttk.Label(tabulador, text="Nombre")
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        def enviar():
            messagebox.showinfo("Mensaje", f"Nombre: {entrada1.get()}")
        boton1 = ttk.Button(tabulador, text="Enviar", command=enviar)
        boton1.grid(row=1, column=0, columnspan=2)

    def _crear_componentes_tabulador2(self, tabulador):
        contenido = "Este es mi texto con el contenido"
        scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        scroll.grid(row=0, column=0)

    def _crear_componentes_tabulador3(self, tabulador):
        datos = [x+1 for x in range(100, 110)]
        combobox = ttk.Combobox(tabulador, width=15, values=datos)
        combobox.grid(row=0, column=0, padx=10, pady=10)
        combobox.current(5)
        def mostrar_valor():
            messagebox.showinfo("Valor seleccionado", f"Valor seleccionado: {combobox.get()}")
        boton1 = ttk.Button(tabulador, text="Mostrar valor seleccionado", command=mostrar_valor)
        boton1.grid(row=0, column=1)

    #def crear_componentes_tabulador4(tabulador):
    #    imagen = tk.PhotoImage(file="942290.png")
    #    def mostrar_titulo():
    #        messagebox.showinfo("Mas info imagen", f"Nombre imagen: {imagen.cget("file")}")
    #    boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
    #    boton_imagen.grid(row=0, column=0)

    def _crear_componentes_tabulador5(self, tabulador):
        barra_progeso = ttk.Progressbar(tabulador, orient="horizontal", length=550)
        barra_progeso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        def ejecutar_barra():
            barra_progeso["maximum"] = 100
            for valor in range(101):
                sleep(.05)
                barra_progeso["value"] = valor
                barra_progeso.update()
            barra_progeso["value"] = 0

        def ejecutar_ciclo():
            barra_progeso.start()

        def detener_ciclo():
            barra_progeso.stop()

        def detener_despues():
            esperar_ms = 1000
            self.after(esperar_ms, barra_progeso.stop)

        boton_inicio  = ttk.Button(tabulador, text="Ejecutar Barra de progreso", command=ejecutar_barra)
        boton_inicio.grid(row=1, column=0)
        boton_ciclo = ttk.Button(tabulador, text="Ejecutar ciclo", command=ejecutar_ciclo)
        boton_ciclo.grid(row=1, column=1)
        boton_detener = ttk.Button(tabulador, text="Detener ciclo", command=detener_ciclo)
        boton_detener.grid(row=1, column=2)
        boton_despues = ttk.Button(tabulador, text="Detener ejecución después", command=detener_despues)
        boton_despues.grid(row=1, column=3)

    def _crear_tabs(self):
        control_tabulador = ttk.Notebook(self)
        tabulador1 = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador1, text="Tabulador 1")
        control_tabulador.pack(fill="both")
        self._crear_componentes_tabulador1(tabulador1)
        tabulador2 = ttk.LabelFrame(control_tabulador, text="Contenido")
        control_tabulador.add(tabulador2, text="Tabulador 2")
        self._crear_componentes_tabulador2(tabulador2)
        tabulador3 = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador3, text="Tabulador 3")
        self._crear_componentes_tabulador3(tabulador3)
        #tabulador4 = ttk.LabelFrame(control_tabulador, text="Contenido")
        #control_tabulador.add(tabulador4, text="Tabulador 4")
        #crear_componentes_tabulador4(tabulador4)
        tabulador5 = tk.LabelFrame(control_tabulador, text="Progress Bar")
        control_tabulador.add(tabulador5, text="Tabulador5")
        self._crear_componentes_tabulador5(tabulador5)

if __name__ == "__main__":
    componentes_ventana = ComponentesVentana()
    componentes_ventana.mainloop()
