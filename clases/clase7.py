"""
i = 1
while i < 6:
    print(i)
    i += 1
"""

# Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número. 

"""
num=int(input("Digíte un número entero positivo: "))

cuenta=2
while cuenta<=num:
    print(cuenta)
    cuenta +=2
"""

#Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.

"""
num=int(input("Digíte un número entero positivo para saber cuantos dígitos tiene: "))
numInicial=num
cuenta=0

while num>1:
    cuenta +=1
    num=num/10

print("El número",numInicial, "tiene", cuenta, "dígitos.")
"""

#Escribe el código que solicite números al usuario hasta que éste ingrese -1.
#Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).

"""
print("Ingrese los números que desee, cuando digíte -1, el programa mostrará el promedio de los números que ingresó")


num=""
total=0
cuenta=0


while num!=-1:
    num=(int(input("Ingrese un número: ")))
    if num!=-1:
        total=total+num
        cuenta+=1
    else:
        promedio=total/cuenta
        print("Usted digitó", cuenta, "números, y el promedio es: ", promedio)
"""