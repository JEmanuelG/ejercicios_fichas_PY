'''
 Se cargan por teclado las notas obtenidas por un estudiante en tres parciales 
realizados durante el cursado de una materia universitaria. Además, se carga la nota final que ese 
estudiante obtuvo en el desarrollo de los trabajos prácticos en esa misma materia. Se sabe que al 
terminar el cursado de la materia, todo alumno puede quedar en uno de los siguientes estados 
académicos:
a. Libre: si no llegó a cumplir con las condiciones para ser Regular.
b. Regular: si aprobó al menos dos de los tres parciales con nota de 4 o más y además obtuvo 
nota de 4 o más en la nota final de trabajos prácticos.
c. Promocionado: si aprobó los tres parciales con nota de 7 o más pero con promedio entre ellos 
de 8(ocho) o más, y además obtuvo nota de 8 o más en la nota final del práctico.
d. Aprobado: si aprobó los tres parciales con nota de 7 o más pero con promedio entre ellos de 
9(nueve) o más, y además obtuvo nota de 8 o más en la nota final del práctico.
El programa debe determinar y mostrar por pantalla el estado en que finalmente quedó el estudiante.
'''
# Define variables
condicion = None
p1 = p2 = p3 = 0
tp_final = 0
promedio = 0

#Ingresa datos por teclado
print("Ingrese notas del alumno")
p1 = int(input("1er parcial:"))
p2 = int(input("2do parcial:"))
p3 = int(input("3er parcial:"))
tp_final = int(input("Final de TP:"))

# Compara notas para establecer la condicion del alumno
if (p1 >= 7) and (p2 >= 7) and (p3 >= 7):
    promedio = round(((p1 + p2 + p3) / 3), 2)
    if (promedio >= 9) and (tp_final >= 8):
        condicion = "Aprobado"
    elif (promedio >= 8) and (tp_final >= 8):
        condicion = "Promocionado"
# En caso de no tener todas las notas mayores o iguales a 7 entre en este else
else:
    if p1 >= 4 or p2 >= 4 or p3 >= 4:
        if p1 >= 4 and p2 >= 4 and tp_final >= 4:
            condicion = "Regular"
        elif p1 >= 4 and p3 >= 4 and tp_final >= 4:
            condicion = "Regular"
        elif p2 >= 4 and p3 >= 4 and tp_final >= 4:
            condicion = "Regular"
        else:
            condicion = "Libre"

# Muestra resultado en consola
print("La condición del alumno es", condicion)