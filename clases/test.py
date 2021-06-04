from random import randint

x=int(input("Cuantas filas? "))
y=int(input("CUantas columnas? "))

def crearMatriz(m,n):
    A=[]
    for i in range(m):
        I=[]
        for j in range(n):
            I.append(randint(0,9))
        A.append(I)
    return A

crearMatriz(x,y)
