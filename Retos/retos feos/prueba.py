import os
os.system("cls")
def bubbleSort(arr, l1):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                l1[j], l1[j+1] = l1[j+1], l1[j]  
    return arr, l1
n=int(input())
#pf_matriz=[]
#tf_matriz=[]
pmit=[]
tmit=[]
tf1=0
tf2=0
tf3=0
tf4=0
pf1=0
pf2=0
pf3=0
pf4=0
sa=0
moa=0
ma=0
na=0
f1=[]
#ingresar datos de temperatura y convertirlo en matriz
for i in range(n):
    b=[]
    t_datos=[]
    for j in range (1):
        c=input().split(' ')
        for k in range (len(c)):
            t_datos.append (float(c[k]))
    tmit.append(t_datos)
#ingresar datos de presion y convertirlo en matriz
for i in range(n):
    d=[]
    p_datos=[]
    for j in range (1):
        e=input().split(' ')
        for k in range (len(e)):
            p_datos.append (float(e[k]))
    pmit.append(p_datos)
for i in range (n):
    f=[0, 0, 0, 0]
    for j in range(len(tmit[0])):
        t=tmit[i][j]
        p=pmit[i][j]
        if t<64 or t>90:
            t=4
            tf4+=1     
        elif t>75 and t<=82:
            t=1
            tf1+=1
        elif (t>82 and t<=86) or (t<=75 and t>68) :
            t=2
            tf2+=1
        elif (t>86 and t<=90) or (t<=68 and t>=64) :
            t=3
            tf3+=1
        if p<4 or p>12.5:
            p=4
            pf4+=1
        elif  p<=8.4 and p>=6:
            p=1
            pf1+=1
        elif  (p>8.4 and p<=10.4) or (p<6 and p>=5):
            p=2
            pf2+=1
        elif  (p>10.4 and p<=12.5) or (p<5 and p>=4):
            p=3
            pf3+=1
        if t==p:
            if t==1:
                sa+=1
                f[0]+=1
            elif t==2:
                moa+=1
                f[1]+=1
            elif t==3:
                ma+=1
                f[2]+=1
            elif t==4:
                na+=1
                f[3]+=1
        if t<p:
            if p==1:
                sa+=1
                f[0]+=1
            elif p==2:
                moa+=1
                f[1]+=1
            elif p==3:
                ma+=1
                f[2]+=1
            elif p==4:
                na+=1
                f[3]+=1
        if t>p:
            if t==1:
                sa+=1
                f[0]+=1
            elif t==2:
                moa+=1
                f[1]+=1
            elif t==3:
                ma+=1
                f[2]+=1
            elif t==4:
                na+=1
                f[3]+=1
        #print(f"dato de la fila {i} con columna{j} {tmit[i][j]}")
    f1.append(f)
print(f1)
print(na, ma, moa, sa)


#tf_datos=[tf1, tf2, tf3, tf4]
#tf_relacion=["sumamente apto", "moderadamente apto", "marginalmente apto", "no apto"]
#pf_datos=[pf1, pf2, pf3, pf4]
#pf_relacion=["sumamente apto", "moderadamente apto", "marginalmente apto", "no apto"]
#t_ordenamiento,t_ordenamiento_relacion=bubbleSort(tf_datos, tf_relacion)
#f_ordenamiento,f_ordenamiento_relacion=bubbleSort(pf_datos, pf_relacion)

#print(f"{t_ordenamiento_relacion[0]},{t_ordenamiento_relacion[1]},{t_ordenamiento_relacion[2]},{t_ordenamiento_relacion[3]}")
#print(f"{f_ordenamiento_relacion[0]},{f_ordenamiento_relacion[1]},{f_ordenamiento_relacion[2]},{f_ordenamiento_relacion[3]}")



    





