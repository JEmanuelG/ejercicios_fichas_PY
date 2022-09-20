'''
Cargar por teclado un conjunto de números enteros, uno a uno. La carga sólo debe 
terminar cuando se ingrese el cero. Determine si los números que se ingresaron eran todos positivos 
o todos negativos (sin importar en qué orden hayan entrado). Por ejemplo, la secuencia {8, 4, 3, 7} 
cumple con la consigna indicada (son todos positivos). La secuencia {-2, -1, -5} también cumple (son 
todos negativos), pero esta otra secuencia {10, -8, 2, 12} no cumple (hay números de distinto signo 
entremezclados). Si todos los números eran efectivamente del mismo signo, muestre también la suma 
de esos números (no mostrar la suma si había números de signos diferentes entremezclados).
'''
# Define variables
num = 0
positivos_flag = negativos_flag = True
suma = 0

# Carga de datos
num = int(input("Ingrese un numero (Con cero corta):"))

while num != 0:
    # Estos ifs ponen las banderas en falso cuando se cumple alguna de sus condiciones
    if num > 0:
        negativos_flag = False

    elif num < 0:
        positivos_flag = False
    
    suma += num
    num = int(input("Ingrese otro número (Con cero corta):"))


# Muestra resultados segun el valor de las banderas
if positivos_flag and not negativos_flag:
    print("Los numeros cargados eran todos positivos.\nLa suma de todos los números cargados es:", suma)

elif negativos_flag and not positivos_flag:
    print("Los numeros cargados eran todos negativos.\n La suma de todos los números cargados es:", suma)
# Si las dos banderas son falsas es porque se cargaron números positivos y negativos
else:
    print("Los números cargados eran de distintos signos.")