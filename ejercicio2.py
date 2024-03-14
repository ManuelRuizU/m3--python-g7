#import math
from math import pow, sqrt, pi
#Tipo de Datos
entero = 7
decimal = 9.5
cadena = " esto es una cadena "
booleanos = True

print(type(entero))
print(type(decimal))
print(type(cadena))
print(type(booleanos))

#precision de datos
promedio = (4+5+7)/3
print(f"el promedio es {promedio}")
print("----------------")
print(f"resulta de la division {1/9:.4f}")
print("----------------")
print(f"resulta de la division {round(1/9,3)}")
print("----------------")
print(f"resulta de la division {promedio:.2f}")
print("----------------")
print (f"resulta de la division {round (promedio,3)}")
print("***********************")
print("***********************")

# Solicitar al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print("  ")
print("******** Tu informacion ingresada es ***************")
print(f"Tu nombre es: {nombre}")
print(f"Tu edad es: {edad}")
print("****************************************************")
print("  ")

print (math.pow(4,2))







