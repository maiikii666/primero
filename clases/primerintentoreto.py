"""
tMA=float(input("Digite la Temperatura Media Anual: "))
pMA=float(input("Digite el valor de la precipitación Anual: "))

if (tMA>76 and tMA<82)and(pMA>6 and pMA<8.4):
    print("Sumamente apto")
elif ((tMA>83 and tMA<86) or (tMA>69 and tMA<75)) and ((pMA>8.5 and pMA<10.4) or (pMA>5 and pMA<5.9)):
    print("Moderadamente apto")
elif ((tMA>87 and tMA<90) or (tMA>64 and tMA<68)) and ((pMA>10.5 and pMA<12.5) or (pMA>4 and pMA<4.99)):
    print("Marginalmente apto")
elif (((tMA>87 and tMA<90) or (tMA>64 and tMA<68)) or ((pMA>10.5 and pMA<12.5) or (pMA>4 and pMA<4.99))) and ((tMA>69 and tMA<86) or (pMA>5 and pMA<10.4)):
    print("Marginalmente apto")
elif (((tMA>83 and tMA<86) or (tMA>69 and tMA<75)) or ((pMA>8.5 and pMA<10.4) or (pMA>5 and pMA<5.9))) and ((tMA>76 and tMA<82) or (pMA>6 and pMA<8.4)):
    print("Moderadamente apto")
else:
    print("No apto")"""



"""
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
    print("No apto")"""




temperatura=int(input("Temperatura Media Anual "))
precipitacion=float(input("Precipitacion Anual "))

if (temperatura<64 or temperatura>90) or (precipitacion<4 or precipitacion>12.5):
    print("No apto")
else:
    if ((87<=temperatura<=90) or (64<=temperatura<=68)) or ((10.5<=precipitacion<=12.5) or (4<=precipitacion<=4.99)):
        print("Marginalmente apto")
    elif ((83<=temperatura<=86) or (69<=temperatura<=75)) or ((8.5<=precipitacion<=10.4) or (5<=precipitacion<=5.9)):
        print("Moderadamente apto")
    else:
        print("Sumamente apto")


"""
valor1=float(input("Digite la temperatura media anual, en unidades °F: "))
valor2=float(input("Digite la precipitacion anual, en unidades de pies:"))

if valor1>=76 and valor1<=82:
   if valor2>=6.0 and valor2<=8.4:
      print("sumamente apto")
   if ((valor2>=8.5 and valor2<=10.4) or (valor2>=5.0 and valor2<=5.9)):
      print("moderadamente apto")
   if ((valor2>=10.5 and valor2<=12.5) or (valor2>=4.0 and valor2<=4.99)):
      print("marginalmente apto")
   if (valor2<4.0 or valor2>12.5):
      print("no apto")
elif (valor1>=83 and valor1<=86 or valor1>=69 and valor1<=75):
   if valor2>=6.0 and valor2<=8.4:
      print("sumamente apto")
   if ((valor2>=8.5 and valor2<=10.4) or (valor2>=5.0 and valor2<=5.9)):
      print("moderadamente apto")
   if ((valor2>=10.5 and valor2<=12.5) or (valor2>=4.0 and valor2<=4.99)):
      print("marginalmente apto")
   if (valor2<4.0 or valor2>12.5):
      print("no apto")
elif (valor1>=87 and valor1<=90 or valor1>=64 and valor1<=68):
   if valor2>=6.0 and valor2<=8.4:
      print("sumamente apto")
   if ((valor2>=8.5 and valor2<=10.4) or (valor2>=5.0 and valor2<=5.9)):
      print("moderadamente apto")
   if ((valor2>=10.5 and valor2<=12.5) or (valor2>=4.0 and valor2<=4.99)):
      print("marginalmente apto")
   if (valor2<4.0 or valor2>12.5):
      print("no apto")
elif (valor1<64 or valor1>90):
   print("no apto")
   """