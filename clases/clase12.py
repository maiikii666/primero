#Escribamos un programa que nos permita crear con una lista de 6 números aleatorios entre 1 y 20, 
#y luego creemos tres funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos
#    orden(x) - Una función que ordene los datos de una lista x ascendentemente y la imprima en orden


"""
from random import randint

lista=[]
while len(lista)<6:
    lista.append(randint(1,20))

print("Numeros generados al azar:", lista)

def mayor(x, a):
    may=x[0]
    for i in range(len(x)):
        if x[i]>may:
            may=x[i]
    if a==1:
        print("El número mayor es: ",may)
    return may
    
def primos(x):
    prim=[]
    def valida(m):                   
        for j in range(2,m):
            if m%j==0:
                return False
        return True
    for i in range (len(x)):
        if valida(x[i])==False:
            continue
        else:
            prim.append(x[i])
    print("Los números primos en la lista son: ",prim)

def ordenar(x):
    print(sorted(x))


mayor(lista,1)
primos(lista)
ordenar(lista)

"""


v=[2,5,7,4,8,1,3,6]

print(v)

###suma de los valores de una lista

suma=0
for i in range(len(v)):
    suma+=v[i]

###suma de las posiciones pares

sumaPosPar=0
for i in range(1,len(v),2):
    sumaPosPar+=v[i]

###suma de los valores pares

sumaPares=0
for i in range(len(v)):
    if v[i]%2==0:
        sumaPares+=v[i]

###corre valores a la izquierda

for i in range(2):
    n=v[0]
    v.append(n)
    v.remove(n)

print(v)

###corre valores a la derecha

for i in range(3):
    n=v[(len(v))-1]
    v.insert(0,n)
    v.pop()

print(v)

print(suma, sumaPosPar, sumaPares)

