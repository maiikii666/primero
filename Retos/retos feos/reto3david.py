def funcionclasificacion(valor1,valor2):
  temp=float(valor1)
  prec=float(valor2)
  claseT=""
  claseP=""
  if temp>75.0 and temp<=82.0:
    claseT="sumamente apto"
  elif temp>82.0 and temp<=86.0:
    claseT="moderadamente apto" 
  elif temp>68.0 and temp<=75.0:
    claseT="moderadamente apto"
  elif temp>86.0 and temp<=90.0:
    claseT="marginalmente apto"  
  elif temp>=64.0 and temp>=68:
    claseT="marginalmente apto"
  else:
    claseT="no apto"
  if prec>=6.0 and prec<=8.4:
    claseP="sumamente apto"
  elif prec>8.4 and prec<=10.4:
    claseP="moderadamente apto" 
  elif prec>=5.0 and prec<6.0:
    claseP="moderadamente apto"
  elif prec>10.4 and prec<=12.5:
    claseP="marginalmente apto"  
  elif prec>=4.0 and prec<5.0:
    claseP="marginalmente apto"
  else:
    claseP="no apto"
  if claseT=="no apto" or claseP=="no apto":
     clase="no apto"
  elif claseT=="marginalmente apto" or claseP=="marginalmente apto":
     clase="marginalmente apto"
  elif claseT=="moderadamente apto" or claseP=="moderadamente apto":
     clase="moderadamente apto"
  elif claseT=="sumamente apto" and claseP=="sumamente apto":
     clase="sumamente apto"
  return clase
def funcionpromedio(listan):
  sumatoria=0
  for i in range(len(listan)):
    sumatoria=sumatoria + listan[i]
  promedio=sumatoria/len(listan)
  return promedio
n=int(input())
promediosT=[]
promediosP=[]
c=1
while c <= n:
  c+=1
  lista1=input().split(" ")
  for j in range(len(lista1)):
    lista1[j]=int(lista1[j])
  fpromT=funcionpromedio(lista1)
  #fpromT='{:.2f}'.format(fpromT)
  promediosT.append(fpromT)
 
  lista2=input().split(" ")
  for j in range(len(lista2)):
    lista2[j]=float(lista2[j])
  fpromP=funcionpromedio(lista2)
  #fpromP='{:.2f}'.format(fpromP)
  promediosP.append(fpromP)
sumapt=0
modapt=0
marapt=0
noapt=0
for i in range(n):
  clasedupla=funcionclasificacion(promediosT[i],promediosP[i])
  if clasedupla=="sumamente apto":
    sumapt+=1
  elif clasedupla=="moderadamente apto":
    modapt+=1
  elif clasedupla=="marginalmente apto":
    marapt+=1
  elif clasedupla=="no apto":
    noapt+=1

promredT=[]
promredP=[]
for i in range(len(promediosT)):
  almpromt="{:.2f}".format(promediosT[i])
  almpromp="{:.2f}".format(promediosP[i])
  promredT.append(almpromt)
  promredP.append(almpromp)

#print(*promediosT, sep = " ")
#print(*promediosP, sep = " ")
print(*promredT, sep = " ")
print(*promredP, sep = " ")
print("sumamente apto %d" %sumapt)
print("moderadamente apto %d" %modapt)
print("marginalmente apto %d" %marapt)
print("no apto %d" %noapt)