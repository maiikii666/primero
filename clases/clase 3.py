print("Bienvenido a la suma, quieres empezar? ")
respuestaUsuario=str(input())
if respuestaUsuario=="si":
    print("Digita el primer número: ")
    primerNumero=float(input())
    print("Digita el segundo número: ")
    segundoNumero=float(input())

    resultado=primerNumero+segundoNumero

    print("Tu respuesta es: ",int(resultado)," Gracias por venir")
else:
    print("Vuelve pronto.")
