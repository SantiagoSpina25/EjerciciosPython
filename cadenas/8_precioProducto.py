#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input("Introduce precio de un producto con dos decimales: ")

print("Euros: " + precio[:precio.find(".")] + "\nCentimos: " + precio[precio.find("."):])