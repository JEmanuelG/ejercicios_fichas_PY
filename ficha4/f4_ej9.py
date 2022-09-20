'''
Cargar por teclado tres números enteros. Determinar si el primero que se cargó es el 
mayor de los tres (informe en pantalla con un mensaje tal como: Es el mayor o No es el mayor).
'''
#definicion de variables
n1 = n2 = n3 = 0

#carga de datos
print("Ingrese los datos")
n1 = int(input("1er número:"))
n2 = int(input("2do número:"))
n3 = int(input("3er número:"))

#procesos / muestra resultado
if (n1 > n2) and (n1 > n3):
    print("El 1er núm cargado es el mayor.")
else:
    print("El 1er núm NO es el mayor.")