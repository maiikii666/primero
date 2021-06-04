from random import randint

def crearMatriz(m,n):
    A=[]
    for i in range(m):
        I=[]
        for j in range(n):
            I.append(randint(0,9))
        A.append(I)
    return A

def imprimeMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def calcularPromedio(T):
    promedio=0
    suma=0
    for i in range (len(T)):
        for j in range(len(T[i])):
            suma+=T[i][j]
    promedio=suma/(len(T[i])*len(T))
    return promedio

x=int(input("Cuantas filas? "))
y=int(input("CUantas columnas? "))

def actividad2(m,n):
    B=[]
    B=crearMatriz(m,n)
    print("Matriz inicial: ")
    imprimeMatriz(B)
    C=calcularPromedio(B)
    D=[]
    for i in range (len(B)):
        F=[]
        for j in range(len(B[i])):
            if B[i][j]>C:
                F.append(1)
            else:
                F.append(0)
        D.append(F)
    print("Promedio: ")
    print(C)
    print("Si el elemento es mayor que el promedio, imprime 1, de lo contrario, imprime 0.")
    imprimeMatriz(D)

actividad2(x,y)

###Cuál es el problema?
###Cuál es la salida?
###Cuales son los procesos? (Cómo utilizo los datos de entrada para producir las salidas)
###Cuales son las entradas?