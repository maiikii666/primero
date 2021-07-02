"""
Matrices o vectores bidimensionales

Vamos a continuar con el trabajo de matrices usando lista de listas. 
Como vimos en la sesión anterior, las operaciones de este tipo de matrices se pueden realizar con ciclos anidados.
"""
"""
numero=int(input("Dígame cuantas palabras tiene la lista: "))

if numero < 1:
    print("Elige un número mayor a 0")
else:
    lista=[]
    for i in range(numero):
        print("Dígame la palabra", str(i+1)+": ", end="")
        palabra=input()
        lista.append(palabra)
    print("La lista creada es:", lista)
"""



#Actividad 1

#Escribe una función actividad1(x) que imprima la diagonal principal de una matriz x. 
#Asegúrate de validar si la matriz es cuadrada, sino devuelve un mensaje, "La matriz no es cuadrada"


#actividad1([[1,1],[2,7,2],[3,3,3]])

from random import randint

def actividad1(a):
    diagonal=[]
    for i in range (len(a)):
        for j in range (len(a[i])):
            if i==j:
                diagonal.append(a[i][j])
    print(diagonal)

def diagonalinvert(a):
    diagonal=[]
    for i in range (len(a)-1,-1,-1):
        for j in range (len(a[i])-1,-1,-1):
            if i==j:
                diagonal.append(a[i][j])
    print(diagonal)

def llenamatriz(x,y,X):
    for i in range(0,x):
        I=[]
        for j in range(0,y):
            I.append(randint(1,100))
        X.append(I)
    return X

f=int(input("Digíte el número de filas: "))
c=int(input("Digíte el número de columnas: "))

if f!=c:
    print("La matríz debe ser cuadrada.")
else:
    a=[]
    a=llenamatriz(f,c,a)
    for i in range(len(a)):
        print(a[i])
    print("La diagonal es: ")
    actividad1(a)
                



#Actividad 2
#
#Creemos ahora una función actividad2() que reciba los elementos de una matriz 3x3 e imprima:
#
#   - La primera fila
#   - La primera columna
#   - Accede al elemento en la fila 1, columna 1.
#
#Los valores son ingresados por filas [0][1], [0][2], [0][3], [1][0], etc


#actividad2()

def actividad2(X):
    print("La primera fila es: ",X[0])
    columna=[]
    for i in range(len(X)):
        columna.append(X[i][0])
    print("La primera columna es: ", columna)
    print("El elemento en la posición 1 para fila y columna es: ",X[1][1])

actividad2(a)
print("La diagonal invertida es: ")
diagonalinvert(a)