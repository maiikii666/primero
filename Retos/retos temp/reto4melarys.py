import os
os.system("cls")
#Quitar el contenido de los inputs
num=int(input("Ingrese el número de datos: "))
vectort=[]
vectorp=[]
vectormax=[]
vectormin=[]
massumamenteapto=0
masmoderadamenteapto=0
masmarginalmenteapto=0
masnoapto=0

def real(z):
    for i in range (len(z)):
        z.append(float(z.pop(0)))
    return z


for i in range (num):
    temp=input()
    temp=temp.split()
    temp=real(temp)   ###########Puse la función aquí para que vectort sean float
    vectort.append(temp)

for i in range (num): 
    precip=input()
    precip=precip.split()
    precip=real(precip)  #### Aquí puse la función para que vectorp sea float
    vectorp.append(precip)

"""
for i in range(len (temp)):
    for j in range(len(temp[i])):
        temp[i][j]=int(temp[i][j])
        precip[i][j]=float(precip[i][j])


print(temp)
print(precip)
"""
"""
print(vectort)
print(vectorp)
"""

def maximo(a,b,c,d):
    if a>=b and a>=c and a>=d:
        return "sumamente apto"
    elif b>a and b>=c and b>=d:
        return "moderadamente apto"
    elif c>a and c>b and c>=d:
        return "marginalmente apto"
    else:
        return "no apto"

def minimo(a,b,c,d):
    if a==0:
        a=9999
    if b==0:
        b=9999
    if c==0:
        c=9999
    if d==0:
        d=9999
    if a<=b and a<=c and a<=d:
        return "sumamente apto"
    elif b<a and b<=c and b<=d:
        return "moderadamente apto"
    elif c<a and c<b and c<=d:
        return "marginalmente apto"
    else:
        return "no apto"

for i in range(num):  ###Se corrije a num
    sumamenteapto=0
    moderadamenteapto=0
    marginalmenteapto=0
    noapto=0    
    for j in range(len (vectort[i])):  ####se corrige porque temp ahora tiene promedios
        if vectort[i][j]>75 and vectort[i][j]<=82:
            if vectorp[i][j]>=6.0 and vectorp[i][j]<=8.4:
                sumamenteapto+=1
            elif (vectorp[i][j]>8.4 and vectorp[i][j]<=10.4) or (vectorp[i][j]>=5.0 and vectorp[i][j]<6.0):
                moderadamenteapto+= 1 
            elif (vectorp[i][j]>10.4 and vectorp[i][j]<=12.5) or (vectorp[i][j]>=4.0 and vectorp[i][j]<5):
                marginalmenteapto+= 1
            elif (vectorp[i][j]>12.5) or (vectorp[i][j]<4.0):
                noapto+= 1 

        elif (vectort[i][j]>82 and vectort[i][j]<=86) or (vectort[i][j]>68 and vectort[i][j]<=75):
            if vectorp[i][j]>=6.0 and vectorp[i][j]<=8.4:
                moderadamenteapto+= 1
            elif (vectorp[i][j]>8.4 and vectorp[i][j]<=10.4) or (vectorp[i][j]>=5.0 and vectorp[i][j]<6.0):
                moderadamenteapto+= 1 
            elif (vectorp[i][j]>10.4 and vectorp[i][j]<=12.5) or (vectorp[i][j]>=4.0 and vectorp[i][j]<5):
                marginalmenteapto+= 1
            elif (vectorp[i][j]>12.5) or (vectorp[i][j]<4.0):
                noapto+= 1

        elif (vectort[i][j]>86 and vectort[i][j]<=90) or (vectort[i][j]>=64 and vectort[i][j]<=68):
            if vectorp[i][j]>=6.0 and vectorp[i][j]<=8.4:
                marginalmenteapto+=1
            elif (vectorp[i][j]>8.4 and vectorp[i][j]<=10.4) or (vectorp[i][j]>=5.0 and vectorp[i][j]<6.0):
                marginalmenteapto+= 1
            elif (vectorp[i][j]>10.4 and vectorp[i][j]<=12.5) or (vectorp[i][j]>=4.0 and vectorp[i][j]<5):
                marginalmenteapto+= 1
            elif (vectorp[i][j]>12.5) or (vectorp[i][j]<4.0):
                noapto+= 1 

        elif (vectort[i][j]>90) or (vectort[i][j]<64):
            if vectorp[i][j]>=6.0 and vectorp[i][j]<=8.4:
                noapto+= 1
            elif (vectorp[i][j]>8.4 and vectorp[i][j]<=10.4) or (vectorp[i][j]>=5.0 and vectorp[i][j]<6.0):
                noapto+= 1
            elif (vectorp[i][j]>10.4 and vectorp[i][j]<=12.5) or (vectorp[i][j]>=4.0 and vectorp[i][j]<5):
                noapto+= 1
            elif (vectorp[i][j]>12.5) or (vectorp[i][j]<4.0):
                noapto+= 1 
        else:
            pass
    vectormax.append(maximo(sumamenteapto,moderadamenteapto,marginalmenteapto,noapto))
    vectormin.append(minimo(sumamenteapto,moderadamenteapto,marginalmenteapto,noapto))
  
#for i in range(num):            ###Este for no se necesita
    massumamenteapto+=sumamenteapto
    masmoderadamenteapto+=moderadamenteapto
    masmarginalmenteapto+=marginalmenteapto
    masnoapto+=noapto
"""
    if sumamenteapto>=moderadamenteapto and sumamenteapto>=marginalmenteapto and sumamenteapto>=noapto:
        vectormax.append("sumamente apto")
    elif moderadamenteapto>=sumamenteapto and moderadamenteapto>=marginalmenteapto and moderadamenteapto>=noapto:
        vectormax.append("moderadamente apto")
    elif marginalmenteapto>=sumamenteapto and marginalmenteapto>=moderadamenteapto and marginalmenteapto>=noapto:
        vectormax.append("marginalmente apto")
    else:
        vectormax.append("no apto")

    if sumamenteapto<=moderadamenteapto and sumamenteapto<=marginalmenteapto and sumamenteapto<=noapto and sumamenteapto!=0:
        vectormin.append("sumamente apto")
    elif moderadamenteapto<=sumamenteapto and moderadamenteapto<=marginalmenteapto and moderadamenteapto<=noapto and moderadamenteapto!=0:
        vectormin.append("moderadamente apto")
    elif marginalmenteapto<=sumamenteapto and marginalmenteapto<=moderadamenteapto and marginalmenteapto<=noapto and marginalmenteapto!=0:
        vectormin.append("marginalmente apto")
    else:
        vectormin.append("no apto")
"""

print(masnoapto, masmarginalmenteapto, masmoderadamenteapto, massumamenteapto)

print(*vectormax, sep=",")
print(*vectormin, sep=",")