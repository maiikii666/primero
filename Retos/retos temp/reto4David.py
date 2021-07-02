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
  elif temp>=64.0 and temp<=68:
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

nzonas=int(input())

matrizTorigen=input()
matrizPorigen=input()

lista1 = matrizTorigen.split(' ')
lista2 = matrizPorigen.split(' ')

matrizTarreglada = []
matrizParreglada = []

for i in range(nzonas):
  l1temp=[]
  l2temp=[]
  for j in range(7):
    l1temp.append(int(lista1[(7*i)+j]))
    l2temp.append(float(lista2[(7*i)+j]))
  matrizTarreglada.append(l1temp)
  matrizParreglada.append(l2temp)

sumapt=0
modapt=0
marapt=0
noapt=0

lmaxmin=[]


for i in range(nzonas):
  l1temp=[0,0,0,0]
  for j in range(7):
    clasedupla=funcionclasificacion(matrizTarreglada[i][j],matrizParreglada[i][j])
    if clasedupla=="sumamente apto":
      sumapt+=1
      l1temp[3]+=1
    elif clasedupla=="moderadamente apto":
      modapt+=1
      l1temp[2]+=1
    elif clasedupla=="marginalmente apto":
      marapt+=1
      l1temp[1]+=1
    elif clasedupla=="no apto":
      noapt+=1
      l1temp[0]+=1
  lmaxmin.append(l1temp)

print(noapt,marapt,modapt,sumapt)

maxlista=[]
minlista=[]

for i in range(nzonas):
  listaindexmax=[index for index,value in enumerate(lmaxmin[i]) if value==max(lmaxmin[i])]
  indexmax=max(listaindexmax)

  if indexmax==0:
    catmax="no apto"
  elif indexmax==1:
    catmax="marginalmente apto"
  elif indexmax==2:
    catmax="moderadamente apto"
  elif indexmax==3:
    catmax="sumamente apto"
  maxlista.append(catmax)
print(maxlista)

lmaxminalt=[]

for i in range(nzonas):
  I=[]
  for j in range(4):
    c=lmaxmin[i][j]
    if lmaxmin[i][j]==0:
      c=1000
    I.append(c)
  lmaxminalt.append(I)

for i in range(nzonas):
  listaindexmin=[index for index,value in enumerate(lmaxmin[i]) if value==min(lmaxminalt[i])]

  indexmin=max(listaindexmin)
  if indexmin==0:
    catmin="no apto"
  elif indexmin==1:
    catmin="marginalmente apto"
  elif indexmin==2:
    catmin="moderadamente apto"
  elif indexmin==3:
    catmin="sumamente apto"
  minlista.append(catmin)
print(minlista)
