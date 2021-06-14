from tkinter import *

root=Tk()

root.title("Prueba de aplicación.")

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miLabel=Label(miFrame, text="Hola, estoy haciendo pruebas")

miLabel.place(x=100, y=200)



root.mainloop()