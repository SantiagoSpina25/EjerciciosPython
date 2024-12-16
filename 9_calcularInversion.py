#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidadAInvertir = float(input("Cuanto queres invertir? "))
interesAnual = float(input("Interes anual? "))
numeroDeAnios = float(input("Numero de años? "))

capitalObtenido = round(cantidadAInvertir * (interesAnual/100 + 1) ** numeroDeAnios,2)
print("El capital obtenido de la inversion es: " + str(capitalObtenido))

