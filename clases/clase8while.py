"""
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
"""

# Continuemos integrando los conceptos que hemos visto hasta el momento. 
# Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número pero que termine el proceso si llega al 10.

"""
num=int(input("Digíte un número entero positivo: "))

cuenta=2
while cuenta<=num:
    print(cuenta)
    cuenta +=2
    if cuenta==10:
        break
"""


"""
i = 1
while i < 6:
    if i == 3:
        i += 1 
        continue
    print(i)
    i += 1
"""


#Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario pero saltarse si el digito es 4.


"""
num=int(input("Digíte un número entero positivo para saber cuantos dígitos tiene exceptuando el 4: "))
numInicial=num
cuenta=0

while num>=1:
    if num%10==4:
        num=num/10
        continue
    cuenta +=1
    num=num/10

print("El número",numInicial, "tiene", cuenta, "dígitos.")
"""


"""
num=float((input("Por favor ingrese numero")))

i=1
print(num, num%10,i)

while num//10>0:
  res=num%10
  num=num//10
  i+=1
  print(num, res,i)
  if res==4:
    i=i-1
    continue
    print(num, res,i)
  
  
print("Tenemos %d dígitos" %i)
"""

"""
num=int(input("Digíte un número entero positivo para saber cuantos dígitos tiene exceptuando el 4: "))
numInicial=num
cuenta=0

while num!=0:
    di=num%10
    num=num//10
    if di==4:
        continue
    cuenta +=1


print("El número",numInicial, "tiene", cuenta, "dígitos.")
"""