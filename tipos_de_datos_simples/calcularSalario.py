#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

numHoras = int(input("Cuantas horas trabajaste? "))

costeHoras = float(input("Cuanto te pagan por hora? "))

print("En total cobraste " + str(numHoras*costeHoras) + " pesos.")
