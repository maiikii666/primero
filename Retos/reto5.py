archivo=open('c:/Users/User/OneDrive/Escritorio/programación/Retos/data.csv', 'r')

##############Poner la ruta relativa
x=archivo.readlines()  ###Lee el archivo completo

def fun1(x):   ###Adapta las listas del archivo a lo que necesito.
    I=[]
    for i in range(1,len(x)):  ### desde 1 para ignorar el titulo
        J=x[i].split(",")   ###Separa la lista
        L=[]
        L.append(J[0])   ### Mete la ciudad
        f=float(J[3])
        L.append(f)  ###Mete la temperatura
        g=float(J[4])
        L.append(g)  ###Mete la precipitación
        L.append(J[6])  ### Mete la condición del campo
        I.append(L)
    return(I)

matrizCompleta=fun1(x)

def fun2(lista,x):
    sumatemp=0
    sumaprec=0
    cuenta=0
    temps=[]
    precs=[]
    suma=0
    mode=0
    marg=0
    noap=0
    promtemp=0
    promprec=0
    for i in range(len(lista)):
        if lista[i][0]==x:
            sumatemp+=lista[i][1]
            sumaprec+=lista[i][2]
            cuenta+=1
            temps.append(lista[i][1])
            precs.append(lista[i][2])
            if lista[i][3]=="sumamente apto\n":
                suma+=1
            elif lista[i][3]=="marginalmente apto\n":
                marg+=1
            elif lista[i][3]=="moderadamente apto\n":
                mode+=1
            elif lista[i][3]=="no apto\n":
                noap+=1
        else:
            continue
    promtemp=sumatemp/cuenta
    promprec=sumaprec/cuenta
    return [temps,precs,promtemp,promprec,noap,marg,mode,suma]
    

x=input()         ##############Pregunta ciudad
definicion=[]
definicion=fun2(matrizCompleta,x) #0. todas las temp 1. todas las prec 2. promtemp, 3.promprec 4, noap,5. marg. 6. mode. 7. sumame

valorMinT=min(definicion[0])
valorMinP=min(definicion[1])
valorMaxT=max(definicion[0])
valorMaxP=max(definicion[1])

organiza=[]


print(round(definicion[2],2), round(definicion[3],2))
print(round(valorMinT), round(valorMinP,2))
print(round(valorMaxT), round(valorMaxP,2))
print("no apto", definicion[4])
print("marginalmente apto", definicion[5])
print("moderadamente apto", definicion[6])
print("sumamente apto", definicion[7])

###PRUEBAS
"""
print(len(matrizCompleta))
print(matrizCompleta[0])
print(matrizCompleta[1])
print(definicion[2],definicion[3],definicion[4],definicion[5],definicion[6],definicion[7])

print(valorMinT,valorMinP,valorMaxT,valorMaxP)
"""