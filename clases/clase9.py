"""
palabra = "Prueba"
longitud = len(palabra)

print("Primer ciclo")
for i in range(longitud):
    print(palabra[i])

print("Segundo ciclo")
for x in "Prueba":
    print(x)
"""
    # Vamos a realizar un algoritmo que nos calcule la serie de Fibonacci.
    # La serie o secuencia de Fibonacci comienza con los números 0 y 1 y 1, y a partir de allí es posible calcular el siguiente valor como la suma de los dos valores anteriores. 
    # Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc. Así, los primeros números de la secuencia son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    # Creemos un programa que a partir de un número N ingresado, imprima los primeros N números de la serie de Fibonacci.

"""

n=int(input("caracteres de fibonacci"))
n=n-3

a=(0)
b=(1)
c=(1)

print(a)
print(b)
print(c)

for i in range(n):
    a=b
    b=c
    c=b+a
    print(c)

"""

    #Escribe el código usando break que reciba una palabra e imprima el número de letras que tiene y las letras hasta que, o bien termine la palabra o encuentre la letra a. .

"""
palabra=input("Ingrese una palabra: ")
longitud=len(palabra)
cuenta=0
var=("en total")


for i in range(longitud):
    if palabra[i]=="a":
        print("Se encontró la palabra a")
        var="antes de la letra a"
        break
    else:
        print(palabra[i])
        cuenta+=1
print("La palabra", palabra, "tiene ", cuenta, "caracteres", var)
"""

    #Escribe un algoritmo que lea 10 números e imprima cuantos son positivos, cuantos negativos y cuantos neutros(0).

"""
print("Se le pediran 10 números, el programa dirá cuantos son neg, pos, o 0")

neg=0
pos=0
neu=0

for i in range(10):
    numero=int(input("Escriba un número: "))
    if numero>0:
        pos+=1
    elif numero==0:
        neu+=1
    else:
        neg+=1

print("Usted digitó, ", pos, "números positivos,", neg, "números negativos y", neu, "ceros")
"""

    #Usando tanto while como for, escribe el codigo que pida números al usuario hasta que este ingrese -1 y que retorne el factorial de cada número ingresado usando un ciclo Para (For).


num=0

while num!=-1:
    num=int(input("Digite número para saber su factorial: "))
    if num!=-1:
        fac=1
        for i in range(num,1,-1):
            print("Voy por el: ", i)
            fac=fac*i
        print(fac)
print("adios")
