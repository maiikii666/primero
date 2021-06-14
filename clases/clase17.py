### Sistema para LactoCaribe

from random import randint

asignacion=[]
registro=[]
eficienciaLista=[]
tasaEntregaLista=[]
nivCumplomiento=[]
matrizCompleta=[]

def vaciaMatriz(matriz):
    matriz=[]
    return matriz

def imprimeMatriz(matriz):
    for i in range(len(matriz)):
        print(*matriz[i], sep="      ")

def asigna():
    I=[]
    #puntoDist=input("Ingrese el punto de distribución: ")
    I.append(randint(200,210))
    #identiCamion=input("Ingrese identificación del camión: ")
    I.append(randint(100,105))
    #cantiLitrosAsig=float(input("Ingrese la cantidad de litros asignados: "))
    I.append(randint(10,50))
    #tiempoDespaAsig=float(input("Ingrese el tiempo asignado en minutos: "))
    I.append(randint(20,120))
    return I
    
def registra(A,i):
    I=[]
    #puntoDist=input("Ingrese el punto de distribución: ")
    I.append(A[i][0])
    #identiCamion=input("Ingrese identificación del camión: ")
    I.append(A[i][1])
    #cantiLitrosDesp=float(input("Ingrese la cantidad de litros despachados: "))
    I.append(randint(10,A[i][2]))
    #tiempoDespaReg=float(input("Ingrese el tiempo registrado en minutos: "))
    I.append(randint(20,140))
    return I

def inicio():
    print("\nBienvenido LactoCaribe al programa \nEstas son las opciones: \n1 Para ingresar una asignación \n2 Para ingresar un registro \n3 Imprimir matriz de asignación \n4 Imprimir matriz de registro \n5 Análisis de eficiencia")
    bienve=int(input("Ingrese la opción deseada: "))
    if bienve==1:
        n=int(input("Ingrese cantidad de datos a ingresar: "))
        for i in range(n):
            asignacion.append(asigna())
        inicio()
    elif bienve==2:
        n=int(input("Ingrese cantidad de datos a ingresar: "))
        for i in range(n):
            registro.append(registra(asignacion,i))
        inicio()
    elif bienve==3:
        imprimeMatriz(asignacion)
        inicio()
    elif bienve==4:
        imprimeMatriz(registro)
        inicio()
    elif bienve==5:
        menu2()

def eficiente(A,B,i):
    f=0
    f=(B[i][3]/A[i][3])*100
    return f

def tasaEntrega(B,i):
    tasa=B[i][2]/B[i][3]
    return tasa

def nivelCumpli(A,B,x):
    cumple=(B[x][2]/A[x][2])*100
    return cumple

def matrizFinal(A,B,C,D,E):
    F=[]
    F.append(["Pun", "Cam", "L/A", "T/A", "L/D", "T/R", "E%", "T/E", "Ni%"])
    for i in range(len(B)):
        I=[]
        I.append(B[i][0])
        I.append(B[i][1])
        I.append(A[i][2])
        I.append(A[i][3])
        I.append(B[i][2])
        I.append(B[i][3])
        I.append(round(C[i],2))
        I.append(round(D[i],2))
        I.append(round(E[i],2))
        F.append(I)
    return F

def menu2():
    print("\nAhora podemos analizar la eficiencia de los camiones \nEstas son las opciones: \n1. Eficiencia en tiempos de despacho \n2. Tasa de entrega \n3. Nivel de cumplimiento de los despachos \n4. Imprimir matriz de asignación \n5. Imprimir matriz de registro \n6. Imprimir matriz completa")
    opcion=int(input("Digíte la opción deseada: "))
    if opcion==1:
        for i in range(len(registro)):
            x=int(i)
            eficienciaLista.append(eficiente(asignacion,registro,x))
        print(" ")
        for i in range(len(registro)):
            print("La eficiencia del camión", registro[i][1], " en el punto ", registro[i][0] , "es: ", round(eficienciaLista[i],2),"%" )
        menu2()
    elif opcion==2:
        for i in range(len(registro)):
            x=int(i)
            tasaEntregaLista.append(tasaEntrega(registro,x))
        print(" ")
        for i in range(len(registro)):
            print("La tasa de entrega del camión", registro[i][1], " en el punto ", registro[i][0] ,"es: ", round(tasaEntregaLista[i],2))
        menu2()
    elif opcion==3:
        for i in range(len(registro)):
            x=int(i)
            nivCumplomiento.append(nivelCumpli(asignacion,registro,x))
        print(" ")
        for i in range(len(registro)):
            print("El nivel de cumplimiento del camión", registro[i][1], " en el punto ", registro[i][0] ,"es: ", round(nivCumplomiento[i],2),"%")
        menu2()
    elif opcion==4:
        imprimeMatriz(asignacion)
        menu2()
    elif opcion==5:
        imprimeMatriz(registro)
        menu2()
    elif opcion==6:
        matrizCompleta=matrizFinal(asignacion,registro,eficienciaLista,tasaEntregaLista,nivCumplomiento)
        imprimeMatriz(matrizCompleta)
        menu2()

inicio()
menu2()
