#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

numBarrasDuras = int(input("Introduce el numero de barras que no son del dia "))
descuento = 0.6
precioBarras = 3.49

costeFinal = round(numBarrasDuras * (precioBarras - (precioBarras * descuento)),2)

print("El precio habitual de una barra de pan es: "+str(precioBarras)+"$ cada una \n El descuento es de "+str(descuento*100)+"% \n El coste final total es: " + str(costeFinal))


