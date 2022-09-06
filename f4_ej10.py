'''
Cargar por teclado tres números enteros que se supone representan las edades de 
tres personas. Determinar si alguno de los valores cargados era negativo, en cuyo caso informe en 
pantalla con un mensaje tal como: Alguna es incorrecta: negativa. Si todos los valores eran positivos 
o cero, informe que todas eran correctas.
'''
#definicion de variables
edad1 = edad2 = edad3 = 0

#carga de datos
print("Ingresa los datos")
edad1 = int(input("Edad de 1ra persona:"))
edad2 = int(input("Edad de 2da persona:"))
edad3 = int(input("Edad de 3ra persona:"))

#proceso
if (edad1 < 0) or (edad2 < 0) or (edad3 < 0):
    print("Alguna es incorrecta: negativa.")
else:
    print("Todas eran correctas.")