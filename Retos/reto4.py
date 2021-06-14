datos=int(input())
temp=[]
prec=[]

def real(z):
    for i in range (len(z)):
        z.append(float(z.pop(0)))
    return z

def listas(a):
    c=(input())
    A=[]
    A=c.split()
    real(A)
    a.append(A)
    return(a)

def masPresente(a,b,c,d):
    if a>=b and a>=c and a>=d:
        return "sumamente apto"
    elif b>a and b>=c and b>=d:
        return "moderadamente apto"
    elif c>a and c>b and c>=d:
        return "marginalmente apto"
    else:
        return "no apto"

def menosPresente(a,b,c,d):
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

def recibeLista(a,A):
    for i in range(a):
        listas(A)
    return A

recibeLista(datos,temp)
recibeLista(datos,prec)

mayor=[]
menor=[]

def clasificacion(a,A,B):
    resulta=[]
    k=0
    l=0
    m=0
    n=0
    for i in range(a):
        sumo=0
        mode=0
        marg=0
        noap=0
        for j in range(len(A[i])):
            if (64<=A[i][j]<=90) and (4<=B[i][j]<=12.5):
                if (68<A[i][j]<=86) and (5<=B[i][j]<=10.4):
                    if (75<A[i][j]<=82) and (6.0<=B[i][j]<=8.4):
                        k+=1
                        sumo+=1
                    else:
                        l+=1
                        mode+=1
                else:
                    m+=1
                    marg+=1
            else:
                n+=1
                noap+=1
        mayor.append(masPresente(sumo,mode,marg,noap))
        menor.append(menosPresente(sumo,mode,marg,noap))
    resulta.extend([k,l,m,n])
    return resulta

cuentageneral=clasificacion(datos,temp,prec)

print(cuentageneral[3],cuentageneral[2],cuentageneral[1],cuentageneral[0])

print(*mayor, sep=",")
print(*menor, sep=",")