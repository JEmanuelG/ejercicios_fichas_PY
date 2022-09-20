'''
Un polinomio de segundo grado tiene la forma p(x) = ax2 + bx + c donde a, b, y c son 
valores constantes conocidos como los coeficientes del polinomio y x es la variable independiente. Se 
supone que el coeficiente a es diferente de cero (pues de lo contrario el término ax2 desaparece y el 
polinomio se convierte en un de primer grado). 
Si el polinomio se iguala a cero, se obtiene una ecuación de segundo grado: ax2 + bx + c = 0 y 
resolver la ecuación es el proceso de hallar los valores de x que hacen que efectivamente el polinomio 
valga cero. 
Por el Análisis Matemático se sabe que todo polinomio de grado n tiene exactamente n raíces (reales 
y/o complejas) para su ecuación y por lo tanto, una ecuación de segundo grado tiene dos raíces a las 
que tradicionalmente se designa como x1 y x2. El problema de encontrar estos dos valores fue 
estudiado desde varios siglos antes de Cristo al menos por los babilonios, los indios y los árabes (de 
hecho, nuestro ya conocido Al-Jwarizmi contribuyó de forma significativa) y la fórmula de cálculo es 
bien conocida: BASKARA
El valor de x1 se obtiene usando el signo + (más) en el numerador, y el valor de x2 se obtiene usando 
el signo – (menos). Desarrolle un programa que dados los valores de los coeficientes a, b y c (y 
suponiendo que a será diferente de cero) calcule y muestre las dos raíces x1 y x2 de la ecuación, 
incluso si las mismas son complejas. El programa debe permitir resolver más de una ecuación: al 
finalizar con una de ellas, el mismo programa debe preguntar al usuario si desea continuar con otra, y 
en ese caso cargar otro juego de coeficientes y volver a resolver.
'''

a = b = c = d = 0
parte_real = parte_imaginaria = 0
x1 = x2 = 0

a = float(input("Ingrese:"))
b = float(input("Ingrese:"))
c = float(input("Ingrese:"))

d = (b**2) - (4*a*c)

if d >= 0:
    x1 = ()/()