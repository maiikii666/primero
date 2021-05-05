tMA=float(input("Digite la Temperatura Media Anual "))
pMA=float(input("Digite el valor de la precipitacion Anual "))

if (64<tMA<90) and (4<pMA<12.5):
    if ((87<tMA<90) or (64<tMA<68)) or ((10.5<pMA<12.5) or (4<pMA<4.99)):
        print("Marginalmente apto")
    elif ((83<tMA<86) or (69<tMA<75)) or ((8.5<pMA<10.4) or (5<pMA<5.9)):
        print("Moderadamente apto")
    else:
        print("Sumamente apto")
else:
    print("No apto")