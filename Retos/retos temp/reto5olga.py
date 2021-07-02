import os
os.system('cls')


import csv

datos=[]

nombre_archivo = "c:/Users/User/OneDrive/Escritorio/programación/Retos/data.csv"
with open(nombre_archivo, "r") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    next(lector, None)


    capital= input("digite la ciudad a verificar: ") 
  
    cont=0
    suma_tem = 0
    suma_preci = 0
    contador = 0
    suapto=0
    morapto=0
    marapto=0
    napto=0 
    listatem=[]         ####Lista que saqué del ciclo for
    listapreci=[]       ####Lista que saqué del ciclo for

    for fila in lector:
        if fila[0]==capital:
           tem = float(fila[3])
           for i in range(len(fila)):    ###Le quité el índice
            listatem.append(float(fila[3]))
           preci = float(fila[4])
           for i in range(len(fila)):       ###Faltaba len            
            listapreci.append(float(fila[4]))      ###Le quite la i
          
           suma_tem += tem
           suma_preci += preci
           contador += 1
           promediop =suma_preci / contador
           promediot =suma_tem / contador


        if fila[0]==capital:
            if fila[6]=="sumamente apto":        
              suapto+=1
            if fila[6]=="marginalmente apto":        
               marapto+=1
            if fila[6]=="moderadamente apto":        
               morapto+=1
            if fila[6]=="no apto":        
               napto+=1

print(f"{promediot:.2f} {promediop:.2f}")
print(round(min(listatem)), min(listapreci))
print(round(max(listatem)), max(listapreci))
print("no apto",napto)   
print("marginalmente apto",marapto)
print("moderadamente apto",morapto) 
print("sumamenteapto",suapto)