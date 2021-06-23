def fun1(ciudad,valor):
    archivo=open('c:/Users/User/OneDrive/Escritorio/programación/Retos/data.csv', 'r')  
    lista1=[]
    x=archivo.readline()
    while x!="":
        x=archivo.readline()
        y=x.split(",")
        if y[0]==ciudad:
            lista1.append(float(y[valor]))
    archivo.close()
    return lista1

def fun2(ciudad,valor):
    archivo=open('c:/Users/User/OneDrive/Escritorio/programación/Retos/data.csv', 'r')
    lista1={"sumamente":0,"marginalmente":0,"moderadamente":0,"noapto":0}
    x=archivo.readline()
    while x!="":
        x=archivo.readline()
        y=x.split(",")
        if y[0]==ciudad:
            if y[valor]=="sumamente apto\n":
                lista1["sumamente"]+=1
            elif y[valor]=="marginalmente apto\n":
                lista1["marginalmente"]+=1
            elif y[valor]=="moderadamente apto\n":
                lista1["moderadamente"]+=1
            elif y[valor]=="no apto\n":
                lista1["noapto"]+=1
    archivo.close()
    return lista1

def promedio(lista):
    suma=0
    for i in range (len(lista)):
        suma+=lista[i]
    promedio=suma/(len(lista))
    return promedio

def salida(diccionario,mayor):
    sumo=diccionario["sumamente"]
    mode=diccionario["moderadamente"]
    marg=diccionario["marginalmente"]
    noap=diccionario["noapto"]
    orden=[]
    orden.extend([sumo,mode,marg,noap])
    orden.sort
    if sumo == orden[mayor]:
        return ["sumamente apto", sumo]
    elif mode == orden[mayor]:
        return ["moderadamente apto", mode]
    elif marg == orden[mayor]:
        return ["marginalmente apto", marg]
    else:
        return ["no apto", noap]

ciudad=input("")

matriz=[]

matriz.append(fun1(ciudad,3))
matriz.append(fun1(ciudad,4))
matriz.append(fun2(ciudad,6))

print(round(promedio(matriz[0]),2),(round(promedio(matriz[1]),2)))
print(round(min(matriz[0])), min(matriz[1]))
print(round(max(matriz[0])), max(matriz[1]))
print(*salida(matriz[2],3), sep=" ")
print(*salida(matriz[2],2), sep=" ")
print(*salida(matriz[2],1), sep=" ")
print(*salida(matriz[2],0), sep=" ")