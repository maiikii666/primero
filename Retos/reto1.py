"""
tMA=float(input("Digite la Temperatura Media Anual "))
pMA=float(input("Digite el valor de la precipitacion Anual "))

if (64<=tMA<=90) and (4<=pMA<=12.5):
    if ((87<=tMA<=90) or (64<=tMA<=68)) or ((10.5<=pMA<=12.5) or (4<=pMA<=4.99)):
        print("Marginalmente apto")
    elif ((83<=tMA<=86) or (69<=tMA<=75)) or ((8.5<=pMA<=10.4) or (5<=pMA<=5.9)):
        print("Moderadamente apto")
    else:
        print("Sumamente apto")
else:
    print("No apto")
"""


datos=(int(input("numero de datos")))


sumApto=0
modApto=0
marApto=0
noApto=0

for i in range (datos):
    temp=(float(input("tempe: ")))
    prec=(float(input("preci: ")))
    if (64<=temp<=90) and (4<=prec<=12.5):
        if (68<temp<=86) and (5<=prec<=10.4):
            if (75<temp<=82) and (6.0<=prec<=8.4):
                print("             sumamente")
                sumApto+=1
            else:
                print("              moderado")
                modApto+=1
        else:
            marApto+=1
            print("            marginal")
    else:
        print("           No apto")
        noApto+=1


print("sumamente apto", sumApto)
print("moderadamente apto", modApto)
print("marginalmente apto", marApto)
print("no apto", noApto)
