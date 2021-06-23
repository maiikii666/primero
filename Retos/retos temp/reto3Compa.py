
n=int(input())
               ###No necesitas iniciar un contador porque estás usando for en todos
sum_p=[]
sum_t=[]
cont_1=0
cont_2=0
cont_3=0
cont_4=0
tma=[]
pa=[]
salida=[]
salida2=[]

def real(lista):
    for i in range (len(lista)):
        lista.append(float(lista.pop(0)))
    return lista

for i in range (n):      
    valor=input() 
    valorSeparados=valor.split()  ##Tienes que separar cada elemento
    valorReales=real(valorSeparados) #### Esta funcion que se define arriba converte cada elemento en float
    tma.append(valorReales)
    # print (i,"tmp")
    valor2=(input())
    valor2Separados=valor2.split()
    valor2Reales=real(valor2Separados)
    pa.append(valor2Reales)
    # print (j,"pa")

def promedio(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    prom=suma/len(lista)
    return prom

for i in range(n):
    prom_tma=promedio(tma[i])    ### Traje una función que saca el promedio
    prom_pa=promedio(pa[i])
    salida.append('%.2f' %prom_tma)
    salida2.append('%.2f' %prom_pa)

    if (prom_tma < 64 ) or (prom_tma > 90) or (prom_pa < 4.0 ) or (prom_pa > 12.5):
       # print("No apto")
        cont_1+=1
    elif (prom_tma >= 64) and (prom_tma <= 68) or (prom_tma > 86) and (prom_tma <= 90) or (prom_pa > 10.4) and (prom_pa <= 12.5) or (prom_pa >= 4.0) and (prom_pa < 5):
        #print("Marginalmente Apto")
        cont_2+=1
    elif (prom_tma > 68) and (prom_tma <= 75) or (prom_tma > 82) and (prom_tma <= 86) or (prom_pa > 8.4) and (prom_pa  <= 10.4) or (prom_pa  >= 5.0) and (prom_pa  <= 5.9):
        #print("Moderadamente Apto")
        cont_3+=1
    elif (prom_tma > 75) and (prom_tma <= 82) or (prom_pa >= 6.0 ) or (prom_pa <= 8.4):
        #print("Sumamente Apto")
        cont_4+=1

   
   # print (salida)
   # print (salida2)
    
print(*salida, sep=" ")
print(*salida, sep=" ")  


print("Sumamente Apto: ",cont_4)
print("Moderadamente Apto: ",cont_3)
print("Marginalmente Apto: ",cont_2)
print("No Apto: ",cont_1)