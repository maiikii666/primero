"""
Manejo de archivos

Vamos ahora a trabajar tanto con archivos de texto como binarios.

En Python, la función open() retorna un objeto tipo archivo. La función recibe dos parámetros que 
incluyen el nombre del archivo y el segundo es la forma en la que se abrirá el archivo, 
el modo (leer, leer y escribir, etc). 

Los siguientes 'modos' pueden ser combinados dependiendo de la operación que se desee realizar. 
Por ejemplo, para leer y escribir un archivo de texto sin eliminar el archivo existente se podría usar 
'r+' y para abrir un archivo binario para lectura usaríamos 'rb'
Modo 	Descripción
'r' 	Abrir el archivo en modo lectura, este es el valor por defecto
'w' 	Abrir el archivo para escritura, eliminará cualquier archivo existente con el mismo nombre
'x' 	Crear el archivo, si existe uno con el mismo nombre sacará un error
'a' 	Abrir el archivo para escribir. Todo lo escrito se adicionará al final del archivo
'b' 	Abrir en modo binario
't' 	Abrir en modo texto, este es el valor por defecto
'+' 	Abrir para lectura y escritura

Crea un archivo de texto llamado miarchivo.txt en notepad y escribe "Esta es una prueba" en la 
primeria línea y "Segunda línea". Guardalo en la carpeta donde esta almacenado este archivo de python. 
Ahora vamos a leer la información del archivo usando la función read().
"""

"""
def ejemplo1():
    miArchivo = open('c:/Users/User/OneDrive/Escritorio/programación/clases/clase 18/miarchivo.txt', 'r')
    informacion = miArchivo.read()
    print(informacion)
"""

#ejemplo1()

#En el siguiente ejemplo, vamos a hacer que el programa lea una línea al tiempo.
"""
def ejemplo2():
    miArchivo = open('c:/Users/User/OneDrive/Escritorio/programación/clases/clase 18/miarchivo.txt', 'r')
    linea = miArchivo.readlines()
    print(linea)
    #print("Lei la primera línea. Vamos a la segunda")
    #linea = miArchivo.readline()
    #print(linea)

ejemplo2()
"""

#Actividad 1
#
#Vamos a trabajar con el archivo matrizAsignacion.txt que está disponible para descargar en la plataforma 
#del curso. Este archivo contiene la información de la matriz de asignación del cliente LactoCaribe 
# []
#
#El objetivo de esta actividad es leer la matriz de asignación y pasar los datos a una matriz en Python 
#como la que veníamos trabajando. 
#
#Finalmente vamos a imprimir la matriz.

asignacionPrimera=[]
asignacion=[]
archivo=open('c:/Users/User/OneDrive/Escritorio/programación/clases/clase 18/matrizAsignacion.txt', 'r')
x=archivo.readlines()
asignacionPrimera.append(x)
print(asignacionPrimera)
print(len(asignacionPrimera))
for i in range(len(asignacionPrimera)):
    I=asignacionPrimera[i].split(",")
    J=[]
    for j in range (len(I)):
        x=float(I[j])
        J.append(x)
    asignacion.append(I)
    print(I)
#print(asignacion)
