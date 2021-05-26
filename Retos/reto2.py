datos=int(input("Ingrese la cantidad de datos que va a ingresar: "))

i=0
temp=0
prec=0

cuentaTemp=0
cuentaPrec=0

sumApto=0
modApto=0
marApto=0
noApto=0

while i<datos:
    temp=float(input("Ingrese la temperatura: "))
    prec=float(input("Ingrese la precipítacion: "))
    cuentaTemp+=temp
    cuentaPrec+=prec
    if (64<=temp<=90) and (4<=prec<=12.5):
        if ((87<=temp<=90) or (64<=temp<=68)) or ((10.5<=prec<=12.5) or (4<=prec<=4.99)):
            marApto+=1
        elif ((83<=temp<=86) or (69<=temp<=75)) or ((8.5<=prec<=10.4) or (5<=prec<=5.9)):
            modApto+=1
        else:
            sumApto+=1
    else:
        noApto+=1
    i+=1

promTemp=float(cuentaTemp/datos)
promPrec=float(cuentaPrec/datos)

print(f"{promTemp:.2f}")
print(f"{promPrec:.2f}")
print("sumamente apto", sumApto)
print("moderadamente apto", modApto)
print("marginalmente apto", marApto)
print("no apto", noApto)
