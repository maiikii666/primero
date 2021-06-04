from random import randint

def llenamatriz(x,y,A):
    for i in range(x):
        I=[]
        m=1
        for j in range(y):
            I.append(m)
            m+=1
        A.append(I)
    return A

def imprimematriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    
def llenamatrizhori(x,y,A):
    m=1
    for i in range(x):
        I=[]
        for j in range(y):
            I.append(m)
        m+=1
        A.append(I)
    return A

def cambiamatrizhori(A):
    I=[]
    for i in range(len(A)):
        B=[]
        for j in range(len(A)):
            B.append(i+1)
        I.append(B)
    return I

def cambiamatrizcuadro(A):
    B=[]
    B.append(A[0])
    for i in range(1,len(A)):
        I=[]
        I.append(A[i][0]+i)
        for j in range(i):
            I.append(A[0][i])
        m=A[i][0]
        while len(I)<len(A):
            I.append(A[i][0]+m+i)
            m+=1
        B.append(I)
    return B

def cambiamatrizcuadroeje(B):
    C=[]
    for i in range(len(B),0,-1):
        J=[]
        J=B[i-1]
        C.append(J)
    return C


def matrizceroyuno(A):
    B=[]
    for i in range(len(A)):
        I=[]
        if i%2==0:
            while len(I)<len(A):
                if len(I)<len(A):
                    I.append(0)
                if len(I)<len(A):
                    I.append(1)
        if i%2==1:
            while len(I)<len(A):
                if len(I)<len(A):
                    I.append(1)
                if len(I)<len(A):
                    I.append(0)

        B.append(I)
    return B



matriz1=[]
print("Cuantas filas y columnas? ")
num=(int(input()))
matriz1=llenamatriz(num,num,matriz1)

imprimematriz(matriz1)

print(" ")


"""
matriz2=[]
matriz2=llenamatrizhori(num,num,matriz2)

imprimematriz(matriz2)
"""

print(" ")
matriz3=[]
matriz3=cambiamatrizhori(matriz1)

imprimematriz(matriz3)

print(" ")

matriz4=[]
matriz4=cambiamatrizcuadro(matriz1)

imprimematriz(matriz4)

print(" ")

matriz5=[]
matriz5=cambiamatrizcuadroeje(matriz4)

imprimematriz(matriz5)

print(" ")


matriz6=[]
matriz6=matrizceroyuno(matriz1)

imprimematriz(matriz6)
