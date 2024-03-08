
"""Tarea 1:

    1.- Leer una cadena
    2.- Imprimir la cadena
    3.- Imprimir la cadena al revez
    4.- Identifiar si es una palabra palindroma

"""

cadena = ("DE TIN MARIN DE DO PINGUE")

print(cadena)

cadena_al_reves = ""
for i in range(len(cadena)-1, -1, -1):
    cadena_al_reves += cadena[i]
print(cadena_al_reves)
"""
1.- Leer un número entre el 1 y el 20
2.- Imprimir un triangulo de numeros con la cantidad de renglones que se respondan.
3.- Ejemplo: 6
1
22
333
4444
55555
666666
"""
numero = int(input("Introduce un número entre 1 y 20: "))
while numero < 1 or numero > 20:
    numero = int(input("Número no válido. Introduce un número entre 1 y 20: "))
for i in range(1, numero + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()
"""
Triangulo de numeros en reversa del 100 a menor cantidad

Ingresa un numero : 6
-0- 100
-6- 94 94
-5- 89 89 89
-4- 85 85 85 85
-3- 82 82 82 82 82
-2- 80 80 80 80 80 80

"""

def imprimir_triangulo(n):
    # Comenzamos con el número más alto
    numero = 100
    
    # Iteramos sobre el rango del número ingresado en orden descendente
    for i in range(n, 0, -1):
        # Construimos la fila con el formato '-i-'
        fila = f"-{n-i}-"
        
        # Repetimos el número actual 'i' veces en la fila
        fila += ' ' + ' '.join([str(numero)] * i)
        
        # Imprimimos la fila
        print(fila)
        
        # Restamos 'i' al número para el siguiente ciclo
        numero -= i

# Solicitamos al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Llamamos a la función para imprimir el triángulo
imprimir_triangulo(numero)