def funcion_conclusion(temp,prec):  #### TE REVISÉ LOS RANGOS DE ACUERDO A LA TABLA QUE TE PASÉ, COMPARALOS
    x=0                             #### ME ESTABA SACANDO ERROR PORQUE NO TENIA X INICIADO ANTES DE COMPARARLO.. NO SE PORQUE A TI NO TE PASABA.
    y=0
    if (temp > 75 and temp <= 82):
        x = 1
        conclusion_1 ="Sumamente Apto"

    if (prec >=6.0 and prec <= 8.4):
        y = 1
        conclusion_2 ="Sumamente Apto"

    if ((temp > 82 and temp <= 86) or (temp > 68 and temp <= 75)):
        x = 2
        conclusion_1 = "Moderadamente Apto" 

    if ((prec > 8.4 and prec <= 10.4) or (prec >= 5.0 and prec < 6.0)):
        y = 2
        conclusion_2 = "Moderadamente Apto"

    if ((temp > 86 and temp <= 90) or (temp >= 64 and temp <= 68)):
        x = 3
        conclusion_1 = "Marginalmente Apto"

    if ((prec > 10.4 and prec <= 12.5) or (prec >= 4.0  and prec < 5.0 )):
        y = 3 
        conclusion_2 ="Marginalmente Apto"

    if (temp < 64 or temp > 90):
        x = 4
        conclusion_1 = "No Apto"

    if (prec > 12.5 or prec < 4.0):
        y = 4
        conclusion_2 = "No Apto"

    if x >= y:
        conclusion_final = conclusion_1 
    else :
        conclusion_final = conclusion_2

    return(conclusion_final)
       
def input_float(lista):
    suma = 0
    x = lista.split()
    cont = len(x)
    for b in range(cont):
        suma += float(x[b])        
    promedio = suma/cont
    return promedio


# INGRESO DE DATOS

promedio_int = []
promedio_float = []

cont_lista = int(input())

# PROMEDIO DE DATOS

for i in range(cont_lista):
    temp = input()
    dato = input_float(temp)
    promedio_int.append(round(dato,2))
    
    precip = input()
    dato_1 = input_float(precip)
    promedio_float.append(round(dato_1,2))

#CONOCIMIENTO DE LOS CASOS

caso_1,caso_2,caso_3,caso_4 = 0,0,0,0

for i in range(cont_lista):
    temp = promedio_int[i]                  ####### AQUÍ LO MODIFIQUE PARA QUE VALIDE EL DATO CON LOS DOS DECIMALES CON LOS QUE SALE DE LA FUNCION QUE PROMEDIA
    prec = promedio_float[i]                ###### AQUÍ TAMBIEN, YA NO SE VA CON UN DECIMAL, SINO CON DOS.
    conclusion = funcion_conclusion(temp,prec)
    
#CONTEO DEL NUMERO DE REPETICIONES DE CADA CASO

    if conclusion == "Sumamente Apto" :
        caso_1 += 1

    if conclusion == "Moderadamente Apto" :
        caso_2 += 1

    if conclusion == "Marginalmente Apto" :
        caso_3 += 1

    if conclusion == "No Apto" :
        caso_4 += 1


# MUESTRA EN FORMATO SPRING LOS PROMEDIOS
resultado_int = ''
resultado_float = ''
for c in range(cont_lista):
    resultado_int += str('{:5.2f}'.format(promedio_int[c])) + " "
    resultado_float += str('{:.2f}'.format(promedio_float[c])) + " "

print(resultado_int)
print(resultado_float)
print("sumamente apto ", caso_1)
print("moderadamente apto", caso_2)
print("marginalmente apto", caso_3)
print("no apto" , caso_4)
    
