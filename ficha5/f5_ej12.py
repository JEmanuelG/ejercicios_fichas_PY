'''
 Una compañía de alquiler de automóviles necesita un programa que calcule lo que se 
debe cobrar a cada cliente, teniendo en cuenta el kilometraje recorrido por el cliente al devolver el 
automóvil: 
i. Si el cliente no superó los 300 km recorridos se deberá cobrar $500. 
ii. Para recorridos desde más de 300 km y hasta no más de 1000 km se le cobrará $500 más el 
kilometraje excedente a los 300, a razón de $3 por kilómetro. 
iii. Para recorridos mayores a 1000 km se le cobrará $500 más el kilometraje excedente a los 
300, a razón de $1.5 por kilómetro
'''

#Importa modulo ramdom
import random

# Define variables
total_a_cobrar = 0
kms_auto = 0

# Define funcion para determinar cuanto se cobra segun kms
def cobro_kilometraje(k):
    # Se resta 300 al kilometraje para obtener solo los kms exedentes
    excedente = k - 300
    monto = 0

    if 0 < k <= 300:
        monto = 500

    elif (300 < k <= 1000):
        monto = excedente * 3 + 500

    # por esta rama entran solo valores mayores a 1000
    else:
        monto = excedente * 1.5 + 500
    # REtorna el monto a cobrar
    return monto

# genera valores aleatorios entre 1 y 5000
kms_auto = random.randint(1, 5000)

# Calcula cuanto se debe cobrar
total_a_cobrar = float(cobro_kilometraje(kms_auto))

# muestra resultados en consola
print("El cliente recorrió {}kms con el auto, se le debe cobrar ${}".format(kms_auto, total_a_cobrar))