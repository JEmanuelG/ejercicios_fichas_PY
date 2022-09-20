'''Se tiene registrada la temperatura ambiente medida en tres momentos diferentes en un 
depósito de químicos y se necesita calcular el valor promedio entre las temperaturas medidas, tanto 
en formato entero (sin decimales) como en formato real (con decimales).'''

#Definicion de variables
temp1 = temp2 = temp3 = 0
promedio_temp_int = promedio_temp_float = 0

#carga de datos
print("Ingresar datos")
temp1 = int(input("Temperatura 1:"))
temp2 = int(input("Temperatura 2:"))
temp3 = int(input("Temperatura 3:"))

#Calculos
suma_temp = temp1 + temp2 + temp3
promedio_temp_int = suma_temp // 3
promedio_temp_float = round((suma_temp / 3), 2)

#muestra resultados
print("Temperatura promedio int:", promedio_temp_int)
print("Temperatura promedio float:", promedio_temp_float)
