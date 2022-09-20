'''Se conoce la cantidad de horas que trabaja un empleado en una fábrica, más el importe 
que percibe por cada hora trabajada, además del nombre del empleado. Se pide calcular el importe 
final del sueldo que el empleado deberá cobrar y mostrar el nombre del empleado y el importe final 
del sueldo que se calculó.'''

#definicion de variables
cant_hs = None
pago_x_hr = None
nombre = None
sueldo = 0

#carga de datos
print("Ingresar datos")
nombre = str(input("Nombre del empleado:"))
cant_hs = int(input("Horas trabajadas:"))
pago_x_hr = float(input("Pago por hora:"))

#calculo del sueldo
sueldo = pago_x_hr * cant_hs

#Muestra resultados
print("El empleado {} debe cobrar un sueldo de ${}".format(nombre, sueldo))