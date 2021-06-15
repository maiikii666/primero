x=int(input())

tem=[]
preci=[]
listapreci=[]    #####ESTAS van afuera del ciclo, para que guarden la info
listatem=[]

def masVeces(a,b,c,d):    ####Esta función la uso para saber de que categoria hay mas
    if a>=b and a>=c and a>=d:
        return "sumamente apto"
    elif b>a and b>=c and b>=d:
        return "moderadamente apto"
    elif c>a and c>b and c>=d:
        return "marginalmente apto"
    else:
        return "no apto"

def menosVeces(a,b,c,d):  ####Esta función la uso para saber de que categoria hay menos
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


for i in range(x):
    temprov= input()                                
    tem=temprov.split()
    I=[]
    for i in range(len(tem)):
        I.append(float(tem[i]))   ###ES MEJOR CON FLOAT
    listatem.append(I)
    
for i in range(x):
    preciprov=input()                             
    preci=preciprov.split()
    J=[]
    for i in range(len(preci)):                 
        J.append(float(preci[i]))
    listapreci.append(J)

matrizResultados=[]

sumo=0     ####Este conteo es para la cuenta de todas las parejas
mode=0
margi=0
noap=0

matrizMasPresente=[]
matrizMenosPresente=[]


for i in range(x):  ##### Este ciclo va a hacer una suma de todas las parejas de valores ingresados
    su=0
    mo=0  ####Este conteo es para ver de cual hay mas o menos en cada zona
    ma=0
    no=0
    dia=len(listatem[i])       ###ES MEJOR CON EL LARGO DE LA LISTA    
    for j in range(dia):   ###Esto se recicla del reto anterior, solo que se cambia el valor que valida.
        if (64<=listatem[i][j]<=90) and (4<=listapreci[i][j]<=12.5):
            if ((86<listatem[i][j]<=90) or (64<=listatem[i][j]<=68)) or ((10.4<listapreci[i][j]<=12.5) or (4.0<=listapreci[i][j]<5.0)):
                ma+=1
                margi+=1
            elif ((82<listatem[i][j]<=86) or (68<listatem[i][j]<=75)) or ((8.4<listapreci[i][j]<=10.4) or (5.0<=listapreci[i][j]<6.0)):
                mo+=1
                mode+=1
            else:
                su+=1
                sumo+=1
        else:
            no+=1
            noap+=1
    matrizMasPresente.append(masVeces(su,mo,ma,no))
    matrizMenosPresente.append(menosVeces(su,mo,ma,no))

matrizResultados.extend([noap,margi,mode,sumo])

print(*matrizResultados, sep=" ")   ###Este método imprime los elementos de una lista sin corchetes, y con la separación que escojas en sep=
print(*matrizMasPresente, sep=",")
print(*matrizMenosPresente, sep=",")