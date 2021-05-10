def actividad3(a, b, opcion):
    print("actividad 3")
    total = 0
    if opcion==1:
        total=a+b
    elif opcion==2:
        total=a*b
    elif opcion==3:
        total=a-b
    elif opcion==4:
        total=a/b


    print("Resultado "+ str(total))


actividad3(4,2,4)