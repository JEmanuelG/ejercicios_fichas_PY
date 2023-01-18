'''
Desarrollar un programa en Python que permita cargar por teclado un texto 
completo (analizar dos opciones: una es cargar todo el texto en una variable de tipo cadena 
de caracteres y recorrerla con un for iterador; y la otra es cargar cada caracter uno por uno a 
través de un while). Siempre se supone que el usuario cargará un punto para indicar el final 
del texto, y que cada palabra de ese texto está separada de las demás por un espacio en 
blanco. El programa debe:
a. Determinar cuántas palabras se cargaron.
b. Determinar cuántas palabras comenzaron con la letra "p".
c. Determinar cuántas palabras contuvieron una o más veces la expresión "ta".
'''
# ASIGNA VARIABLES Y BANDERAS
flag_t = False
flag_ta = False
flag_letra = False
cont_palabras = 0
cont_palabras_p = 0
cont_palabras_ta = 0
text = ''

print('Ingrese opción\n',
      '1) Para analizar texto cargado en una variable\n',
      '2) Cargar texto por teclado')

opcion = int(input('Opción: '))

while opcion < 1 or opcion > 2:
    print('INGRESE UNA OPCIÓN VÁLIDA (1 O 2)')
    opcion = int(input('Opción: '))


if opcion == 1:
    text = 'El siguiente problema está orientado al planteo de una situación clásica como es el procesamiento de una secuencia de caracteres que forman una frase, de forma tal que el programador no sólo debe ser capaz de identificar palabras dentro de esa frase, sino también la formación de ciertos patrones en cada palabra.'

else:
    caracter = ''
    print('Ingrese caracteres uno a uno (Con "." finaliza)')

    while caracter != '.':
        caracter = str(input('Caracter: '))
        text += caracter

print('TEXTO:\n' + text)

# CONVIERTE TODAS LAS LETRAS EN MINUSCULAS
text = text.lower()

for c in text:
    
    # CUANDO EL CARACTER ES IGUAL A UN ESPACIO O PUNTO CUENTA UNA PALABRA
    if c == ' ' or c == '.':
        if flag_letra:
            cont_palabras += 1
            flag_letra = False
            flag_ta = False

        # SI EL CARACTER ES UN PUNTO CORTA CON EL CICLO
        if c == '.':
            break

    else:
        # CUENTA PALABRAS QUE COMIENZAN CON P
        if (not flag_letra) and (c == 'p'):
            cont_palabras_p += 1

        flag_letra = True

        # CUENTA LA CANTIDAD DE PALABRAS QUE CONTIENEN TA
        if c == 't':
            flag_t = True
        
        elif flag_t:
            if (c == 'a') and (not flag_ta):
                cont_palabras_ta += 1
                flag_ta = True
            flag_t = False


# MUESTRA RESULTADOS
print('Cantidad de palabras:', cont_palabras)

print('Cantidad de palabras que comienzan con p:', cont_palabras_p)

print('Cantidad de palabras que contienen ta:', cont_palabras_ta)
