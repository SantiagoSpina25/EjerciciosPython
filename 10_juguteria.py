#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

payasosVendidos = int(input("Cuantos payasos se vendieron? "))
muniecasVendidas = int(input("Cuantas muñecas se vendieron? "))

print("El peso total del paquete será de: " + str((payasosVendidos * 112) + (muniecasVendidas * 75)) + " g")