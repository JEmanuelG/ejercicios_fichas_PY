'''
La dirección de la carrera de Ingeniería en Sistemas de la UTN Córdoba necesita un 
programa que permita cargar el nombre de un estudiante de quinto año, el nombre del profesor 
responsable de la Práctica Profesional Supervisada de ese estudiante, y el promedio general (con 
decimales) del estudiante en su carrera. Una vez cargados los datos, se pide simplemente mostrarlos 
en la consola de salida a modo de verificación, pero de forma que el nombre del practicante vaya 
precedido de la cadena "est." y el nombre del profesor supervisor se preceda con "prof.". El promedio 
del alumno debe mostrarse redondeado, sin decimales, en formato entero.
'''

#definicion de variables
dato_est = dato_prof = None
estudiante = profesor = None
dato_prom = promedio = 0

#carga de datos
print("Carga de datos")
dato_est = str(input("Nombre del estudiante:"))
dato_prof = str(input("Nombre del profesor:"))
dato_prom = float(input("Nota promedio del estudiante:"))

#procesos
estudiante = "est. " + dato_est
profesor = "prof. " + dato_prof
promedio = round(dato_prom)

#muestra resultados
print("Practicante: {}\t-\tPromedio: {}".format(estudiante, promedio))
print("Supervisor: {}".format(profesor))