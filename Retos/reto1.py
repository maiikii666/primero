temperaturaMediaAnual=float(input("Digite la Temperatura Media Anual: "))
precipitacionAnual=float(input("Digite el valor de la precipitación Anual: "))

if temperaturaMediaAnual>=76 and temperaturaMediaAnual<=82:
    if precipitacionAnual>=6.0 and precipitacionAnual<=8.4:
        print("Sumamente Apto")
elif ((temperaturaMediaAnual>=83 and temperaturaMediaAnual<=86) or (temperaturaMediaAnual>=75 and temperaturaMediaAnual<=69)) and ((precipitacionAnual>=8.5 and precipitacionAnual<=10.4) or (precipitacionAnual>=5.0 and precipitacionAnual<=5.9)):
    print("Moderadamente Apto")
elif ((temperaturaMediaAnual>=87 and temperaturaMediaAnual<=90) or (temperaturaMediaAnual>=64 and temperaturaMediaAnual<=68)) and ((precipitacionAnual>=10.5 and precipitacionAnual<=12.5) or (precipitacionAnual>=4.0 and precipitacionAnual<=4.99)):
    print("Marginalmente Apto")
else:
    print("No Apto")