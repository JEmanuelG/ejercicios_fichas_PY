'''Se conoce la cantidad total de personas que padecen cierta enfermedad en todo el 
país, y también se sabe cuántas de esas personas viven en una ciudad determinada. Se desea saber 
qué porcentaje representan estas últimas sobre el total de enfermos del país'''

#Definicion de variables
enfermos_total = enfermos_ciudad = 0
porcentaje = 0

#Carga de datos
print("Cargar datos")
enfermos_total = int(input("Cantidad de enfermos del pais:"))
enfermos_ciudad = int(input("Cantidad de enfermos en la ciudad:"))

#Calculos
porcentaje = round((enfermos_ciudad * 100 / enfermos_total), 2)

#muestra resultados
print("La cantidad de enfermos de la ciudad representa el {}% el total del pais".format(porcentaje))