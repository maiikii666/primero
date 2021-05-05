tMA=float(input("Digite la Temperatura Media Anual "))
pMA=float(input("Digite el valor de la precipitacion Anual "))

if (tMA>64 and tMA<90) and (pMA>4 and pMA<12.5):
    if ((tMA>87 and tMA<90) or (tMA>64 and tMA<68)) or ((pMA>10.5 and pMA<12.5) or (pMA>4 and pMA<4.99)):
        print("Marginalmente apto")
    elif ((tMA>83 and tMA<86) or (tMA>69 and tMA<75)) or ((pMA>8.5 and pMA<10.4) or (pMA>5 and pMA<5.9)):
        print("Moderadamente apto")
    else:
        print("Sumamente apto")
else:
    print("No apto")
