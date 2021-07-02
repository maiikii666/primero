archivo=open("c:/Users/User/OneDrive/Escritorio/programación/clases/clase 20/personas.txt", mode="r", encoding='utf-8-sig')

listaProv=archivo.readlines()

personas=[]

for i in listaProv:
    I={"id":0,"nombre":0,"apellido":0,"nacimiento":0}
    provi=i.split(";")
    I["id"]=provi[0]
    I["nombre"]=provi[1]
    I["apellido"]=provi[2]
    I["nacimiento"]=provi[3].strip()
    personas.append(I)

for i in personas:
    print(i)