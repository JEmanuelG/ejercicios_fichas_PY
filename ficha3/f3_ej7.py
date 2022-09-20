'''
Una pequeña oficina de correos dispone de cinco casillas o boxes para guardar las 
cartas que debe despachar. Cada casilla (que puede contener muchas cartas) está numerada con 
números correlativos del 0 al 4. Cada carta que se recibe tiene un código postal numérico, y en base a 
ese código el despachante debe determinar en qué box guardará la carta, pero de tal forma que el 
mismo sistema sirva luego para saber en qué caja buscar una carta, dado su código postal. Diseñe un 
esquema de distribución que permita cumplir este requerimiento, cargando por teclado el código 
postal de tres cartas y mostrando en qué casilla será almacenada cada una. 
'''
#definicion de variables
carta1 = carta2 = carta3 = 0
cantidad_box = 0
destino1 = destino2 = destino3 = 0

#carga de datos
print("Ingrese los datos")
carta1 = int(input("CP carta 1:"))
carta2 = int(input("CP carta 2:"))
carta3 = int(input("CP carta 3:"))

#procesos
cantidad_box = 5
#tomamos el resto de dividir el cp por la cantidad de boxs disponibles
destino1 = carta1 % cantidad_box
destino2 = carta2 % cantidad_box
destino3 = carta3 % cantidad_box

#Muestra resultados
print("CP: {} fue asignado al box: {}".format(carta1, destino1))
print("CP: {} fue asignado al box: {}".format(carta2, destino2))
print("CP: {} fue asignado al box: {}".format(carta3, destino3))