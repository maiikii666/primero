"""
numUno=int(input("Escriba el primer número: "))
numDos=int(input("Escriba el segundo número: "))
numTres=int(input("Escriba el tercer número: "))

if numUno != numDos and numUno !=numTres and numDos != numTres:
    print("Los tres números son distintos")
elif numUno == numDos and numDos == numTres:
    print("Los tres numeros son iguales")
else:
    print("Hay un número repetido dos veces")
"""

"""
print("Programa para saber si un año es bisiesto")
valor=int(input("Digíte el año: "))

if valor%4!=0:
    print("El año", valor, " no es bisiesto, porque no es multiplo de 4")
elif valor%100==0 and valor%400!=0:
    print("El año", valor, " no es bisiesto, porque es multiplo de 100 pero no de 400")
elif valor%4==0 and valor%100!=0:
    print("El año", valor, " es bisiesto, porque es multiplo de 4 pero no de 100")
else:
    print("El año", valor, "es un año bisiesto, porque es multiplo de 400")
"""

#   1. Leer un número de 4 dígitos, mostrar el dígito mayor e 
#      informar si es par o impar.

"""
print("Digíte cada uno de los dígitos de un número de 4 cifras")

num=float(input("Digite un número de 4 cifras: "))

dig1=int(num%10)
dig2=int((num%100)/10)
dig3=int((num%1000)/100)
dig4=int((num%10000)/1000)

if dig1>=dig2 and dig1>=dig3 and dig1>=dig4:
    if dig1%2==1:
        print("El dígito", dig1, " es el mayor y es impar")
    else:
        print("El dígito", dig1, " es el mayor y es par")
elif dig2>=dig1 and dig2>=dig3 and dig2>=dig4:
    if dig2%2==1:
        print("El dígito", dig2, " es el mayor y es impar")
    else:
        print("El dígito", dig2, " es el mayor y es par")
elif dig3>=dig2 and dig3>=dig1 and dig3>=dig4:
    if dig3%2==1:
        print("El dígito", dig3, " es el mayor y es impar")
    else:
        print("El dígito", dig3, " es el mayor y es par")
elif dig4>=dig1 and dig4>=dig3 and dig4>=dig2:
    if dig4%2==1:
        print("El dígito", dig4, " es el mayor y es impar")
    else:
        print("El dígito", dig4, " es el mayor y es par")
"""

#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
#      con el mayor del primero y el menor del segundo.
"""
print("Este programa forma un tercer número de dos cifras, utilizando el mayor dígito del primero y el menor del segundo.")
num1=float(input("Digite un número de 3 cifras: "))

dig11=int(num1%10)
dig12=int((num1%100)/10)
dig13=int((num1%1000)/100)
digMayorUno=""

num2=float(input("Digite otro número de 3 cifras: "))

dig21=int(num2%10)
dig22=int((num2%100)/10)
dig23=int((num2%1000)/100)


if dig11>=dig12 and dig11>=dig13:
    digMayorUno=dig11
elif dig12>=dig11 and dig12>=dig13:
    digMayorUno=dig12
elif dig13>=dig12 and dig13>=dig11:
    digMayorUno=dig13
    
digMenorDos=""

if dig21<=dig22 and dig21<=dig23:
    digMayorDos=dig11
elif dig22<=dig21 and dig22<=dig23:
    digMayorDos=dig22
elif dig23<=dig22 and dig23<=dig21:
    digMayorDos=dig23

total=10*digMayorUno+digMayorDos
#####    total=100*c1+10*c2+c3
print("Sus números iniciales fueron: ", int(num1), "y ", int(num2), "El tercer número es: ", total)
"""


#   3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.

"""
print("El programa construirá el mayor número posible con las tres cifras que digíte")

num=int(input("Digíte un número: "))

dig1=int(num%10)
dig2=int((num%100)/10)
dig3=int((num%1000)/100)

Frst=""
Scnd=""
Thrd=""

if dig1>=dig2 and dig1>=dig3:
    Frst=dig1
    if dig2>=dig3:
        Scnd=dig2
        Thrd=dig3
    else:
        Scnd=dig3
        Thrd=dig2
if dig2>=dig1 and dig2>=dig3:
    Frst=dig2
    if dig1>=dig3:
        Scnd=dig1
        Thrd=dig3
    else:
        Scnd=dig3
        Thrd=dig1
if dig3>=dig1 and dig3>=dig2:
    Frst=dig3
    if dig2>=dig1:
        Scnd=dig2
        Thrd=dig1
    else:
        Scnd=dig1
        Thrd=dig2
    
total=100*Frst+10*Scnd+Thrd

print("El número inicial era: ", num, " el número final es: ", total)

"""




num=float(input("Digite un número de 4 cifras: "))

dig1=int(num%10)
dig2=int((num%100)/10)
dig3=int((num%1000)/100)
dig4=int((num%10000)/1000)

mayor=""
par=""

if dig1>=dig2 and dig1>=dig3 and dig1>=dig4:
    mayor=dig1
elif dig2>=dig1 and dig2>=dig3 and dig2>=dig4:
    mayor=dig2
elif dig3>=dig2 and dig3>=dig1 and dig3>=dig4:
    mayor=dig3
elif dig4>=dig1 and dig4>=dig3 and dig4>=dig2:
    mayor=dig4

if mayor%2==0:
    par="par"
else:
    par="impar"

print("El mayor dígito es: ",mayor, "y es un número ",par)