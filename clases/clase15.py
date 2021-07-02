from random import randint

def crearMatriz(m,n):
    A=[]
    for i in range(m):
        I=[]
        m=randint(0,9)
        for j in range(n):
            I.append(m)
            m=randint(0,9)
        A.append(I)
    return A

#A=crearMatriz(x,y)

def imprimeMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

#imprimeMatriz(A)

def calcularPromedio(T):
    I=0
    suma=0
    for i in range (len(T)):
        for j in range(len(T[i])):
            suma+=T[i][j]
    I=suma/((len(T))*(len(T[0])))
    return I

#calcularPromedio(A)

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
    print("Promedio de la matríz: ")
    print(C)
    print("Si el elemento es mayor que el promedio, imprime 1, de lo contrario, imprime 0.")
    imprimeMatriz(D)


actividad2(x,y)

"""
###Cuál es el problema?

# Se necesita crear una matríz de x columnas por y filas, 
# se debe llenar con números aleatorios del 1 al 9, 
# sacar el promedio de la matríz y comparar si cada valor 
# es mayor o menor que el promedio.


###Cuál es la salida?

# 1. Una matriz de x filas por y columnas, llena de números 
# aleatorios del 1 al 9, 
# 2. el promedio de la matríz 
# 3. Otra matríz con los valores reemplazados por: 1 si el 
# valor está por encima del promedio o 0 si es inferior al 
# promedio.


###Cuales son los procesos? (Cómo utilizo los datos de 
# entrada para producir las salidas)

# Pregunto el dato de filas y columnas deseadas, genero 
# la matríz rellena con números aleatorios, luego hago una 
# variable que almacene la suma de todos los valores de la 
# matríz y la divido por el total de elementos para tener 
# el promedio, después se lee cada elemento de la matríz 
# y se compara con el promedio para almacenar en una nueva 
# matríz que valida si el valor es menor o mayor que el 
# promedio


###Cuales son las entradas?

#La cantidad de filas y columnas deseadas

"""