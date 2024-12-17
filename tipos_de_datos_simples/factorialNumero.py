#Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta .

numIntroducido = int(input("Introduzca un numero positivo "))

if numIntroducido < 0:
    print("El numero tiene que ser positivo")
else:
    suma = (numIntroducido*(numIntroducido+1))/2
    print(suma) 