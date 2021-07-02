"""
def suma(a,b):
    
    print(a+b)

suma(3,4)
"""

"""
def factorial(a):
    fac=1
    for i in range(a,1,-1):
        fac=fac*i
    return fac

def combinacion(n,m):
    c=0
    facton=factorial(n)
    factom=factorial(m)
    connm=n-m
    factonm=factorial(connm)
    c=facton/(factom*factonm)
    print("La cantidad de combinaciones es ", c)

n=int(input("Tamaño del conjunto: "))
m=int(input("Tamaño del grupo a crear"))
combinacion(n,m)
"""


#Actividad 1
#Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos de su cliente, su precio y calcular el total a pagar.
#
#Diseña un programa con las siguiente características:
#
#    1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
#    2. Una variable total que vaya sumando el precio de los artículos
#    3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
#        el precio de cada producto y los imprima.
#    4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    5. Si no hay más artículos, que imprima el total de la compra

#    Al final de tus funciones, puedes simplement llamar a la función caja para probar

"""
def imprimaProducto(nombre, precio):
    print(nombre, precio)

def caja():
    total=0
    pregunta=input("Va a ingresar algún producto? ")
    while pregunta=="si":
        nombre=input("Digite el nombre del producto: ")
        precio=float(input("Digite el precio del producto: "))
        total+=precio
        imprimaProducto(nombre, precio)
        pregunta=input("Va a ingresar algún producto? ")
    print(total)

caja()
"""


#Actividad 2
#
#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120 .
#
#Adicionalmente, una función numeros que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.

#numeros()



from random import randint, uniform, random
"""
print(randint(0,20))
print(uniform(0,10))
print(random())
"""

def numAleatorio():
    a=randint(100,130)
    while a!=110 or a!=115 or a!=120:
        return(a)

def numeros():
    for i in range(5):
        x=numAleatorio()
        while x%2!=0:
            x=numAleatorio()
        print(x)
        y=numAleatorio()
        while y%2==0:
            y=numAleatorio()
        print(y)

numeros()
