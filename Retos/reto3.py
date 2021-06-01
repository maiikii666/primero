datos=int(input())
temp=[]
prec=[]
promTemp=[]
promPrec=[]
promTempSali=[]
promPrecSali=[]

def promedio(x):
    suma=0
    for i in range(len(x)):
        suma+=x[i]
    prom=suma/len(x)
    return round(prom, 2)

def real(z):
    for i in range (len(z)):
        z.append(float(z.pop(0)))
    return z

def listas(b, c):
    listaNF=(input())
    b=listaNF.split()
    real(b)
    c.append(promedio(b))
    b=[]
    return b, c

def cadena(j,m):
    for i in range (len(j)):
        m.append(('%.2f' %j[i]))
    return m

for i in range(datos):
    listas(temp, promTemp)
    listas(prec, promPrec)

sumApto=0
modApto=0
marApto=0
noApto=0

for i in range(datos):
    if (64<=promTemp[i]<=90) and (4<=promPrec[i]<=12.5):
        if (68<promTemp[i]<=86) and (5<=promPrec[i]<=10.4):
            if (75<promTemp[i]<=82) and (6.0<=promPrec[i]<=8.4):
                sumApto+=1
            else:
                modApto+=1
        else:
            marApto+=1
    else:
        noApto+=1

cadena(promTemp,promTempSali)
cadena(promPrec,promPrecSali)

print(*promTempSali, sep=" ")
print(*promPrecSali, sep=" ")
print("sumamente apto", sumApto)
print("moderadamente apto", modApto)
print("marginalmente apto", marApto)
print("no apto", noApto)