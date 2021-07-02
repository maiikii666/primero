import csv


archivo=open("c:/Users/User/OneDrive/Escritorio/programación/clases/clase19/archivoprueba.csv",mode="w",encoding='utf-8-sig')

escribirArchivo=csv.writer(archivo)
"""
archivo.write("Hola amigos\nSegunda línea")
archivo.writelines("Hola amigos\nLinea con writelines")

archivo.writelines("A ver que pasa, no sé")
archivo.writelines("A ver que pasa, no sé por dooooos")
archivo.write("jajajajajajaj")

archivo.write(str([2,45,6,6,6,6,4,4]))

archivo.writelines("Hola")
"""
fila=[1,2,3,6,5,4]

escribirArchivo.writerow(fila)