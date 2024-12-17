#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> 
#donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

num1 = int(input("Introduzca un numero entero "))
num2 = int(input("Introduzca otro numero entero "))

resto = num1/num2
cociente = num1%num2

print("El resto de la division " + str(num1) + " y " + str(num2) + " es: \n Resto: " + str(resto) + "\n Cociente: " + str(cociente) )