#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Introduzca su peso en kilos: "))
estatura = float(input("Introduce la estatura en metros: "))
imc = peso/(estatura**2)

print("Tu IMC (indice de masa corporal) " + str(round((imc),2)))