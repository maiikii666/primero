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

