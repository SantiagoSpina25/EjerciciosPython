# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario 
# tantas veces como el número introducido.

nombreUsuario = input("Cual es tu nombre? ")
numero = int(input("Introduce numero de veces que queres escribir tu nombre "))

print((nombreUsuario + "\n") * numero)

# for i in range(0, numero):
#     print(nombreUsuario)
