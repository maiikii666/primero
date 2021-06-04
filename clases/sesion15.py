"""
Matrices o vectores bidimensionales

Vamos a utilizar esta sesión para repasar los conceptos vistos y a aprender otras funciones interesantes 
en Python.

La función string.split(), por ejemplo, toma una cadena de caracteres (string) y la pasa a una lista.
Por defecto el separador es cada espacio en blanco, pero se puede seleccionar cualquier separador. 
Veamos un ejemplo:
"""

"""
def ejemplo1(frase):
    lista = frase.split()
    print(lista)

ejemplo1("Esta es una prueba para pasar a una lista")

def ejemplo1comas(frase):
    lista = frase.split(",")
    print(lista)

ejemplo1comas("esta es, una prueba, con comas")
"""

#Actividad 1
#
#Escribe una función actividad1(x, n) que reciba una frase x y un numero entero n 
#e imprima una lista con las palabras cuya longitud sea mayor a n de entrada.

#print(actividad1("Esta es una prueba para pasar a una lista",3))

#Actividad 2
#
#Creemos ahora una función crearMatriz(m,n) que genere una matriz de M * N con números aleatorios 
#entre 0 y 9 y la retorne.
#
#Creemos también una función calcularPromedio(T) que dada una matriz T, genere un promedio de todos 
#sus elementos y lo retorne.
#
#Finalmente una función actividad2(m,n) que llame a crearMatriz, pase esa matriz a calcularPromedio(T) 
#y que genere una matriz que tenga el valor 1 en aquellas posiciones donde el valor sea mayor o igual 
#al promedio en T y cero (0) donde el valor de la posición en T sea menor que el promedio.
#
#Imprimir ambas matrices.

#actividad2(3,3)
"""
frase=input("Escriba una frase: ")
num=int(input("Número: "))

def actividad(x,n):
    lista=x.split()
    listanueva=[]
    for i in range(len(lista)):
        if len(lista[i])>n:
            listanueva.append(lista[i])
    print(listanueva)

actividad(frase, num)
"""


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
    I=[]
    for i in range (len(T)):
        suma=0
        for j in range(len(T[i])):
            suma+=T[i][j]
        promedio=suma/len(T[i])
        I.append(promedio)
    #for i in range(len(I)):
        #print(I[i])
    return I

#calcularPromedio(A)

x=int(input("Cuantas filas? "))
y=int(input("CUantas columnas? "))

def actividad2(m,n):
    B=[]
    B=crearMatriz(m,n)
    print("Matriz inicial: ")
    imprimeMatriz(B)
    C=[]
    C=calcularPromedio(B)
    D=[]
    for i in range (len(B)):
        F=[]
        for j in range(len(B[i])):
            if B[i][j]>C[i]:
                F.append(1)
            else:
                F.append(0)
        D.append(F)
    print("Promedios de cada fila: ")
    imprimeMatriz(C)
    print("Si el elemento es mayor que el promedio, imprime 1, de lo contrario, imprime 0.")
    imprimeMatriz(D)


actividad2(x,y)
