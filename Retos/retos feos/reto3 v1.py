datos=int(input("Ingrese la cantidad de datos que va a ingresar: "))

temp=[]
prec=[]

promTemp=[]
promPrec=[]

sumApto=0
modApto=0
marApto=0
noApto=0

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

for i in range(datos):
    tempNF=(input("Ingrese los datos de temperatura: "))
    temp=tempNF.split()
    real(temp)
    promTemp.append(promedio(temp))
    precNF=(input("Ingrese los datos de precipitación: "))
    prec=precNF.split()
    real(prec)
    promPrec.append(promedio(prec))
    temp=[]
    prom=[]


for i in range(len(promTemp)):
    if (64<=round(promTemp[i])<=90) and (4<=round(promPrec[i],1)<=12.5):
        if ((87<=round(promTemp[i])<=90) or (64<=round(promTemp[i])<=68)) or ((10.5<=round(promPrec[i],1)<=12.5) or (4<=round(promPrec[i],1)<=4.99)):
            marApto+=1
        elif ((83<=round(promTemp[i])<=86) or (69<=round(promTemp[i])<=75)) or ((8.5<=round(promPrec[i],1)<=10.4) or (5<=round(promPrec[i],1)<=5.9)):
            modApto+=1
        else:
            sumApto+=1
    else:
        noApto+=1

print(promTemp)
print(promPrec)
print("sumamente apto", sumApto)
print("moderadamente apto", modApto)
print("marginalmente apto", marApto)
print("no apto", noApto)