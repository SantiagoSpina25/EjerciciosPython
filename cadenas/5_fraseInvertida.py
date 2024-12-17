#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

frase = input("Introduce una frase: ")
print(frase[::-1])

#El [::-1] es una forma de invertir una cadena de texto. Funciona de la siguiente manera:
#El primer : indica que se va a tomar toda la cadena.
#El segundo : es para el paso, y el -1 significa que se toma la cadena en orden inverso.