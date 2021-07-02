#import pywhatkit
from tkinter import *

class VentanaEjemplo:
    def __init__(self, master):
        self.master=master
        master.title("Una simple interfaz gráfica")

        self.etiqueta=Label(master, text="Esta es la primera ventana!")
        self.etiqueta.pack()

        self.botonSaludo=Button(master, text="Saludar", command=self.saludar)
        self.botonSaludo.pack()

        self.botonCerrar=Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()
    
    def saludar(self):
        print("Hey!")

root=Tk()
miVentana=VentanaEjemplo(root)
root.mainloop()

"""
try:
    pywhatkit.sendwhatmsg("+573163997230", "Cuando te llegue vienes y me das un beso", 16,38)
    print("Mensaje enviado")
except:
    print("Ocurrió un error")
"""