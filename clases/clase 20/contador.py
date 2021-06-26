def fun(x,y):
    if y=="inc":
        x+=1
    elif y=="dec":
        x-=1
    return x


try:
    archivo=open("clases/clase 20/contador.txt", mode="x")
    archivo.writelines("0")
except:
    lectura=open("clases/clase 20/contador.txt", mode="r")
    valor=int(lectura.readline())
    orden=input("inc o dec")
    valorFinal=fun(valor,orden)
    escribe=open("clases/clase 20/contador.txt", mode="w")
    escribe.writelines(str(valorFinal))