archivo=open('c:/Users/User/OneDrive/Escritorio/programación/Retos/data.csv', 'r')
x=archivo.readlines()

def fun1(x):
    I=[]
    for i in range(1,len(x)):
        J=x[i].split(",")
        L=[]
        L.append(J[0])
        f=float(J[3])
        L.append(f)
        g=float(J[4])
        L.append(g)
        L.append(J[6])
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

x=input()
definicion=[]
definicion=fun2(matrizCompleta,x)

valorMinT=min(definicion[0])
valorMinP=min(definicion[1])
valorMaxT=max(definicion[0])
valorMaxP=max(definicion[1])

organiza=[]
organiza.extend([definicion[4],definicion[5],definicion[6],definicion[7]])

organizaFinal=[]

for i in range(len(organiza)):
    if organiza[0]>(organiza[1] and organiza[2] and organiza[3]):
        organizaFinal.append(["no apto", organiza[0]])
        organiza[0]=0
    elif organiza[1]>(organiza[0] and organiza[2] and organiza[3]):
        organizaFinal.append(["marginalmente apto", organiza[1]])
        organiza[1]=0
    elif organiza[2]>(organiza[0] and organiza[1] and organiza[3]):
        organizaFinal.append(["moderadamente apto", organiza[2]])
        organiza[2]=0
    elif organiza[3]>(organiza[0] and organiza[1] and organiza[2]):
        organizaFinal.append(["sumamente apto", organiza[3]])
        organiza[3]=0

print(('%.2f' %definicion[2]), ('%.2f' %definicion[3]))
print(round(valorMinT), round(valorMinP,2))
print(round(valorMaxT), round(valorMaxP,2))

print(*organizaFinal[0], sep=" ")
print(*organizaFinal[1], sep=" ")
print(*organizaFinal[2], sep=" ")
print(*organizaFinal[3], sep=" ")