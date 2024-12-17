#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("Introduce el correo electronico: ")
correoNuevo = correo[:correo.find("@")] + "@ceu.es" 
#Toma la parte de la dirección de correo antes del @. Esto se hace mediante rebanado (slicing) de la cadena correo. Es decir, toma todos los caracteres de la dirección de correo hasta justo antes del @.

print(correoNuevo)
