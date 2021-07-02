def Inicio():
    print(
	    "Bienvenido al conversor de unidades, seleccione la opción deseada:\n1. Para convertir medidas de distancia.\n2. Para convertir medidas de volumen\n3. Para convertir medidas de masa\n4. Para envíar un comentario al desarrollador.")
    opcion_uno=int(input("Ingrese la selección: "))
    return opcion_uno

palabras_clave = {"distancias" : 
        {"km" : 
            ["kilometros", "KM", "KILOMETROS", "kms", "km", "KMS", "kilometro", "KILOMETRO", "Kilometro", "Kilometros"] , 
        "dm" : 
            ["decametros", "decametro", "DECAMETRO", "DECAMETROS", "Decametro", "Decametros"] , 
        "m" : 
            ["metros", "metro", "mts", "mt", "METROS", "METRO", "m", "Metro", "Metros"] , 
        "cm" : 
            ["centimetros", "CENTIMETRO", "CM", "cm", "CMS", "cms", "Centimetros", "Centimetro", "centimetro"] , 
        "mm" : 
            ["milimetros", "Milimetro", "MILIMETRO", "milimetro", "Milimetros", "MILIMETROS", "mm", "MM", "Mm", "mms", "MMS", "Mms"] ,
        "mi" : 
            ["millas", "Milla", "MILLA", "milla", "Millas", "MILLAS", "mil", "mi", "MIL", "MI"] ,
        "y" : 
            ["yardas", "Yarda", "YARDA", "yarda", "Yardas", "YARDAS", "yd", "YD", "Yd"] ,
        "ft" :
            ["pies", "PIE", "Pie", "ft", "FT", "Ft", "pie", "PIES", "Pies", "fts", "FTS", "Fts"] ,
        "in" :
            ["pulgadas", "Pulgada", "PULGADA", "pulgada", "Pulgadas", "PULGADAS", "in", "IN", "In"] ,
        "nm" :
            ["millas nauticas", "Milla nautica", "Milla Nautica", "MILLA NAUTICA", "milla nautica", "Millas nauticas", "Millas Nauticas", "MILLAS NAUTICAS", "nm", "NM", "Nm"]
        }
     }

def Ayuda(tipo, campo):
    campo = 0
    if tipo == "distancias":
        ########VOY AQUI MIRAR SE PUEDE HACER MAS CORTA LA PRINT
        print(
            "Estas son las unidades disponibles para conversión de distancias:", dic.keys())
            #\n-Kilometro = km\n-Decametro = dm\n-Metro = m\n-Decimetro=dc\n-Centimetro = cm\n-Milimetro = mm\n-Milla = mi\n-Yarda = y\n-Pie = ft\n-Pulgada = in\n-Milla nautica = nm")
        return campo

def Verifica_unidades(tipo,unidad):   ###Verifica que cumplan con alguna unidad del diccionario
    for key in palabras_clave:
        for key in palabras_clave[tipo]:
            for j in range(len(palabras_clave[tipo][key])):
                if palabras_clave[tipo][key][j] == unidad:
                    return key


def RecibeUnidades(tipo):
    entrada = input(
        "Escriba la medida a convertir, seguida de la unidad, separado por un espacio. Ejemplo: 80 unidad: ")
    if entrada == ("ayuda" or "Ayuda" or "AYUDA"):
        entrada = Ayuda(tipo, entrada)
        entrada = input(
        "Escriba la medida a convertir, seguida de la unidad, separado por un espacio. Ejemplo: 80 unidad: ")
    convertir_a = input(
        "Escriba la unidad en requerida en la salida. Ejemplo: unidad: ")
    if convertir_a == ("ayuda" or "Ayuda" or "AYUDA"):
        convertir_a = Ayuda(tipo, convertir_a)
        convertir_a = input(
        "Escriba la unidad en requerida en la salida. Ejemplo: unidad: ")
    entradas=entrada.split(" ")
    entradas.append(convertir_a)
    return entradas

def ConversorDistancia():
    print(
        "Va a usar el conversor de distancias, si desea consultar las conversiones disponibles, digite: AYUDA.")
    entrada_separada = RecibeUnidades("distancias")
    valor_inicial = entrada_separada[0]
    unidad_inicial = Verifica_unidades("distancias",entrada_separada[1])   ###Verifica unidad de entrada
    convertir_a = Verifica_unidades("distancias",entrada_separada[2])    ###Verifica unidad de salida
    print(unidad_inicial, convertir_a)
    
opcion_uno=Inicio() ####Primera ejecución

if opcion_uno==1:
    ConversorDistancia()