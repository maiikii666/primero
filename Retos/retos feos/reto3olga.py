x=int(input())
limite=1
suapto=0
morapto=0
marapto=0
napto=0
tem=[]
preci=[]
listapromediost=[]
listapromediosp=[]
listatempsalida=[]
listaprecsalida=[]


while (limite<=x):
    limite=limite+1             ###contador del ciclo acomodado
    listatem=[]                 ###cada nuevo ciclo la lista debería quedar vacia para recibir la nueva
    listapreci=[]
    print("ingrese lista temperaturas:")           #### BORRAR!!!!!!!
    temprov= input()                                ###temprov cadena provisional
    tem=temprov.split()
    for i in range(len(tem)):
        listatem.append(float(tem[i]))            ####convierte la temperatura en float     
    print("ingrese lista de precipitacion:")      #### BORRAR!!!!!!!!!!!!
    preciprov=input()                             ####preciprovi provisional cadena
    preci=preciprov.split()
    for i in range(len(preci)):                   ####convierte preci en float
        listapreci.append(float(preci[i]))       ####LISTE
    promediot=0                         ###reinicia el promedio
    promediop=0                 
    sumat=0                             ####reinicia la suma
    sumap=0
    for i in range(len(listatem)):                ####Suma para sacar el promedio de temp
        sumat=sumat+listatem[i]
    promediot=sumat/len(listatem)              ####redondea a dos decimales
    listapromediost.append(round(promediot,2))           ####mete un nuevo promedio en la lista de promedios linea 9
    for i in range(len(listapreci)):             #####suma para sacar el promedio de prec
        sumap=sumap+listapreci[i]
    promediop=sumap/len(listapreci)                ####redondea a dos decimales
    listapromediosp.append(round(promediop,2))       ####mete un nuevo promedio en la lista de promedios linea 10
    if (64<=promediot<=90) and (4<=promediop<=12.5):
        if ((86<promediot<=90) or (64<=promediot<=68)) or ((10.4<promediop<=12.5) or (4.0<=promediop<5.0)):
            marapto+=1
            print("margi")
        elif ((82<promediot<=86) or (68<promediot<=75)) or ((8.4<promediop<=10.4) or (5.0<=promediop<6.0)):
            morapto+=1
            print("mode")
        else:
            suapto+=1
            print("sumo")
            napto=(x-(suapto+morapto+marapto))

for i in range (len(listapromediost)):
    listatempsalida.append(('%.2f' %listapromediost[i])) ####Crea una lista que obliga a que hayan dos decimales
    listaprecsalida.append(('%.2f' %listapromediosp[i]))


print(*listatempsalida, sep=" ")                #####Imprime sin comas y sin corchetes, como lo pide el reto
print(*listaprecsalida, sep=" ")
print("sumamente apto ",suapto)
print("moderadamente apto ", morapto)
print("marginalmente apto",marapto)
print("no apto ",napto)