def fun(x,y):
    if y=="inc":
        x+=1
    elif y=="dec":
        x-=1
    return x


try:
    archivo=open("c:/Users/User/OneDrive/Escritorio/programación/clases/clase 20/contador.txt", mode="x")
    archivo.writelines("0")
except:
    lectura=open("c:/Users/User/OneDrive/Escritorio/programación/clases/clase 20/contador.txt", mode="r")
    valor=int(lectura.readline())
    orden=input("inc o dec")
    valorFinal=fun(valor,orden)
    escribe=open("c:/Users/User/OneDrive/Escritorio/programación/clases/clase 20/contador.txt", mode="w")
    escribe.writelines(str(valorFinal))