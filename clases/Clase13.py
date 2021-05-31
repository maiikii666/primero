"""
print("Multiplicador de matrices")

def multimatriz(A,B,C):
    n=len(A)
    m=len(B)
    for i in range (len(A)):
        for j in range (len(A[i])):
            C[i][j]=(A[i][j]*B[i][j])+A[j][i]*B[j][i]
        return C


A=[[1,2],[3,4],[5,6]]
B=[[1,2,3],[4,5,6]]
C=[]


multimatriz(A,B,C)

print(C)
"""
#Actividad 1
#
#Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y 100
#aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.

from random import randint


def llenamatriz(x,y,X):
    X=[]
    for i in range(0,x):
        I=[]
        for j in range(0,y):
            I.append(randint(1,100))
        X.append(I)
    return X

def mayor(A):
    may=0
    for i in range (len(A)):
        for j in range (len(A[i])):
            if A[i][j]>may:
                may=A[i][j]
    return may

def menor(A):
    men=100
    for i in range (len(A)):
        for j in range (len(A[i])):
            if A[i][j]<men:
                men=A[i][j]
    return men

A=[]
A=llenamatriz(5,10,A)
print(A)
grande=mayor(A)
peque=menor(A)
print("El mayor es: ", grande, "El menor es: ", peque )

#El producto escalar de un número real, x , y una matriz A es la matriz xA. 
#Cada elemento de la matriz xA es x veces su elemento correspondiente en A.
#
#Diseñemos una funcion escalar(matriz, escalar) que dada matriz[n][m] y un escalar, 
#imprima el producto escalar de la matriz.

def escalar(matriz, escalar):
    resultado=[]
    for i in range((len(matriz))):
        parcial=[]
        for j in range(len(matriz[i])):
            parcial.append(matriz[i][j]*escalar)
        resultado.append(parcial)
    return resultado

resultado=[]
n=int(input("Ahora digite a cuanto quiere escalar la matríz anterior: "))
resultado=escalar(A, n)

print("Matríz escalada a ", n)
print(resultado)