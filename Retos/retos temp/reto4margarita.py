datos=int(input())

tempe=[]
precip=[]
lispreci=[]    
listem=[]

def muchas(a,b,c,d):    
    if a>=b and a>=c and a>=d:
        return "sumamente apto"
    elif b>a and b>=c and b>=d:
        return "moderadamente apto"
    elif c>a and c>b and c>=d:
        return "marginalmente apto"
    else:
        return "no apto"

def pocos(a,b,c,d):  
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


for i in range(datos):
    temprov= input()                                
    tempe=temprov.split()
    I=[]
    for i in range(len(tempe)):
        I.append(float(tempe[i]))   
    listem.append(I)
    
for i in range(datos):
    preciprov=input()                             
    precip=preciprov.split()
    J=[]
    for i in range(len(precip)):                 
        J.append(float(precip[i]))
    lispreci.append(J)

matrizResultados=[]

sumo=0     
mode=0
margi=0
noap=0

matrizMasPresente=[]
matrizMenosPresente=[]

for i in range(datos):  
    su=0
    mo=0  
    ma=0
    no=0
    dia=len(listem[i])       
    for j in range(dia):   
        if (64<=listem[i][j]<=90) and (4<=lispreci[i][j]<=12.5):
            if ((86<listem[i][j]<=90) or (64<=listem[i][j]<=68)) or ((10.4<lispreci[i][j]<=12.5) or (4.0<=lispreci[i][j]<5.0)):
                ma+=1
                margi+=1
            elif ((82<listem[i][j]<=86) or (68<listem[i][j]<=75)) or ((8.4<lispreci[i][j]<=10.4) or (5.0<=lispreci[i][j]<6.0)):
                mo+=1
                mode+=1
            else:
                su+=1
                sumo+=1
        else:
            no+=1
            noap+=1
    matrizMasPresente.append(muchas(su,mo,ma,no))
    matrizMenosPresente.append(pocos(su,mo,ma,no))

matrizResultados.extend([noap,margi,mode,sumo])

print(*matrizResultados, sep=" ")   
print(*matrizMasPresente, sep=",")
print(*matrizMenosPresente, sep=",")