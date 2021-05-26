n= int(input())
i=1
sumat=0
sumap=0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
while i<=n:
    tma = int(input())
    pa = float(input())
    if  (tma<64 or tma>90) or (pa<4.0 or pa>12.5) :
        #No apto
        cont1 +=1       
    elif(tma>=76 and tma<=82) and (pa>=6.0 and pa<=8.4) :
        #Sumamente apto
        cont2 +=1        
    elif ((tma>=83 and tma<=86) or (tma>=69 and tma<=75)) or ((pa>=8.5 and pa<=10.4) or (pa>=5.0 and pa<=5.9)) :
        #Moderadamente apto
        cont3 +=1       
    else:
        #Marginalmente apto
        cont4 +=1 
    sumat+= tma
    sumap+= pa
    i+=1  
    prom= sumat/n
    pro= sumap/n
a=round(prom,2)
b=round(pro,2)   
print(a)
print(b)
print(f'sumamente apto {cont2}')
print(f'moderamente apto {cont3}')
print(f'marginalmente apto {cont4}') 
print(f'no apto {cont1}')