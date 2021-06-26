def inicio():
    print("Bienvenido al conversor de unidades, seleccione la opción deseada:\n1. Para convertir medidas de distancia.\n2. Para convertir medidas de volumen\n3. Para convertir medidas de masa\n4. Para envíar un comentario al desarrollador.")
    opcionUno=int(input("Ingrese la selección: "))
    return opcionUno

def ayuda(x):
    if x == 1:
        print("Estas son las unidades disponibles para conversión de distancias:\n-Kilometro = km\n-Decametro = dm\n-Metro = m\n-Decimetro=dc\n-Centimetro = cm\n-Milimetro = mm\n-Milla = mi\n-Yarda = y\n-Pie = ft\n-Pulgada = in\n-Milla nautica = nm")
        conversorDistancia()

###Terminar de completar

def conversorDistancia():
    print("Va a usar el conversor de distancias, si desea consultar las conversiones disponibles, digite: AYUDA.")
    entrada=input("Escriba la medida a convertir, seguida de la unidad, separado por un espacio. Ejemplo: 80 km: ")
    if entrada == "AYUDA" or "ayuda":
        ayuda(1)
    convertirA=input("Escriba la unidad en requerida en la salida. Ejemplo: NM: ")

opcionUno=inicio()

if opcionUno==1:
    conversorDistancia()
