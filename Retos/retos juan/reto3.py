minimo=[]
maximo=[]
diaserror=0
errorcinco=0
errortreinta=0
errorambos=0

minimo.append(int(input()))
maximo.append(int(input()))
while (minimo[len(minimo)-1] and maximo[len(maximo)-1])!=0:
    minimo.append(int(input()))
    maximo.append(int(input()))

dias=(len(maximo)-1)

for i in range(len(minimo)-1):
    if (5>minimo[i] or minimo[i]>35) or (5>maximo[i] or maximo[i]>35):
        diaserror+=1
    if (5>minimo[i] or 5>maximo[i]) and (minimo[i]>35 or maximo[i]>35):
        errorambos+=1
    elif 5>minimo[i] or 5>maximo[i]:
        errorcinco+=1
    elif 35<minimo[i] or 35<maximo[i]:
        errortreinta+=1


listamin=[]
listamax=[]
sumavalidosmin=0
sumavalidosmax=0

for i in range(len(minimo)):
    if 5<=minimo[i]<=35 and 5<=maximo[i]<=35:
        listamin.append(minimo[i])
        sumavalidosmin+=minimo[i]

for i in range(len(maximo)):
    if 5<=maximo[i]<=35 and 5<=minimo[i]<=35:
        listamax.append(maximo[i])
        sumavalidosmax+=maximo[i]

promediomin=sumavalidosmin/(len(listamin))
promediomax=sumavalidosmax/(len(listamax))

if diaserror!=0:
    porcenerror=(diaserror/dias)*100

print(dias)
print(diaserror)
print(errorcinco)
print(errortreinta)
print(errorambos)
print(promediomin)
print(promediomax)
print(round(porcenerror,8))