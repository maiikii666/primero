a = 2
b = 3
c = 1

x1=(-b+((b**2)-(4*a*c))**0.5)/(2*a)
x2=(-b-((b**2)-(4*a*c))**0.5)/(2*a)
print("El resultado de x1 es ", x1)
print(x2)



import math
a = 2
b = 3
c = 1
x1 = (-b + math.sqrt((b**2)-(4*a*c)))/2*a
x2 = (-b - math.sqrt((b**2)-(4*a*c)))/2*a
print(x1)
print(x2)