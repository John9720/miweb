#GUI = Graphical User Interface
#Tkinter = TK Interface
import tkinter as tk
from tkinter import ttk, messagebox, Menu
import sys
from tkinter.ttk import *
import sticky

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x130")
        self.title("Login")
        self.resizable(0, 0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)
        self._crear_componentes()

    def _crear_componentes(self):

        usuario_etiqueta = ttk.Label(self, text="Usuario: ")
        usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        usuario_entrada = ttk.Entry(self)
        usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        password_etiqueta = ttk.Label(self, text="Password: ")
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        password_entrada = ttk.Entry(self, show="*")
        password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        login_boton = ttk.Button(self, text="Login", command=self.login)
        login_boton.grid(row=3, column=0, columnspan=3)

    def login(self):
        messagebox.showinfo("Datos Login", f"Usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}")

if __name__ == "__main__":
    login_ventana = LoginVentana()
    login_ventana.mainloop()