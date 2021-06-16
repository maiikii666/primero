"""
Manejo de archivos

Continuemos ahora con otras opciones como escribir y actualizar un archivo desde Python.

Recordemos las opciones disponibles para el manejo de archivos.
Modo 	Descripción
'r' 	Abrir el archivo en modo lectura, este es el valor por defecto
'w' 	Abrir el archivo para escritura, eliminará cualquier archivo existente con el mismo nombre
'x' 	Crear el archivo, si existe uno con el mismo nombre sacará un error
'a' 	Abrir el archivo para escribir. Todo lo escrito se adicionará al final del archivo
'b' 	Abrir en modo binario
't' 	Abrir en modo texto, este es el valor por defecto
'+' 	Abrir para lectura y escritura

Empecemos creando un archivo de texto llamado minuevoarchivo.txt. 
"""

"""
def ejemplo1():
    nuevoArchivo = open('c:/Users/User/OneDrive/Escritorio/programación/clases/clase19/minuevoarchivo.txt', mode='w', encoding='utf-8-sig' )
    nuevoArchivo.write("Escribiendo desde Python")

"""
#ejemplo1()

#Ahora vamos a crear un diccionario y a imprimir todos los valores y el valor almacenado con la clave 2

def ejemplo2():
    diccionario = { "uno" : 'lunes', "dos":'martes', "tres":'miercoles', "cuatro":'jueves', "cinco":'viernes', "seis":'sabado', "siete":'domingo'}

    print(diccionario)
    print(diccionario["dos"])

#ejemplo2()

# Actividad 1
#
# Vamos a elaborar un algoritmo que permita ingresar un número entero (1 a 10), y muestre su equivalente en romano usando un diccionario como lo definimos anteriormente. 
"""
diccionarioNumeros={1:"I",
2:"II",
3:"III",
4:"IV",
5:"V",
6:"VI",
7:"VII",
8:"VIII",
9:"IX",
10:"X"}

x=int(input("Número para convertir a romano"))
print(diccionarioNumeros[x])
"""

#Actividad 2 
#Recordemos una de las actividades que hicimos en sesiones anteriores.
#
#Diseña un programa con las siguiente características:
#
#    Que tenga una función caja que 
#       a. Cree un archivo recibo.txt
#       b. Solicite al usuario nombre y precio de cada producto.
#       d. Una función adicional llamada guardaProducto(nombre, precio, archivo) que reciba el nombre y el precio de cada producto y los escriba en el archivo recibo.txt.
#       e. Que después de llamar a guardaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    Al final de tus funciones, puedes simplemente llamar a la función caja para probar


def guardaProducto(archivo,x):
    archivo.writelines(str(x))

def caja():
    nuevoArchivo = open('c:/Users/User/OneDrive/Escritorio/programación/clases/clase19/recibo.txt', mode='w', encoding='utf-8-sig')
    instruccion=input("Desea ingresar un producto? ")
    while instruccion == "si":
        nombreYValor={"nombre":0,"valor":0}
        nombreYValor["nombre"]=input("Ingrese el nombre del producto: ")
        nombreYValor["valor"]=float(input("Ingrese el valor del producto: "))
        print(nombreYValor)
        guardaProducto(nuevoArchivo,nombreYValor)
        instruccion=input("Desea ingresar un producto?")
    print("adios")
    nuevoArchivo.close

caja()
miArchivo = open('c:/Users/User/OneDrive/Escritorio/programación/clases/clase19/recibo.txt', mode='r')
print(miArchivo.readlines())
    

