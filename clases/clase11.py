"""
v=[]
n=int(input("digite un numero"))

for i in range(n):
    v.append(int(input("digite un numero")))
print(v)
"""

#números al cuadrado
"""
v=[]
c=[]
n=int(input("Números a ingresar: "))
for i in range (n):
    m=int(input("Digite un número: "))
    v.append(m)
    c.append(v[i]*v[i])
    print(v[i], "al cuadrado es",c[i])
"""

# Usando el conocimiento de ciclos, crea una funcion numeros que tenga una lista con los numeros pares del 1 al 10 
# y usa un ciclo para que los imprima

"""
def numeros():
    pares=[]
    n=2
    while len(pares)<5:
        pares.append(n)
        n+=2
    for j in range(0,5,1):
        print(pares[j])

numeros()
"""

#Escribamos un programa que nos permita crear una lista de 6 números aleatorios entre 1 y 20 en Python, y 
#creemos dos funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos


from random import randint

lista=[]
while len(lista)<6:
    lista.append(randint(1,20))

print("Numeros generados al azar:", lista)

def mayor(x):
    may=x[0]
    for i in range(len(x)):
        if x[i]>may:
            may=x[i]
    print("El número mayor es: ",may)

def primos(x):
    prim=[]
    def valida(m):                    #Verificador de primos :)
        for j in range(2,m,1):
            if m%j==0:
                return False
        return True
    for i in range (len(x)):
        if valida(x[i])==False:
            continue
        else:
            prim.append(x[i])
    print("Los números primos en la lista son: ",prim)
                        
mayor(lista)
primos(lista)