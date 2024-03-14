
#escape.py
# Ejercicio Velocidad de escape.
#rkm = el radio del planeta en kilometros.
#cg = constante g es la aceleración debida a la gravedad en la superficie de un planeta.
#ve = velocidad de escape.

print(' ')
print ('******** Velocidad de escape ********')
print(' ')
print("Por favor, ingrese el radio en kilómetros:")
rkm = float(input("Ingrese el radio en Kilómetros: ")) 
cg = float(input("Ingrese la constante g: "))

# Cálculo de la velocidad de escape
ve = (2 * cg * rkm * 1000) ** 0.5

# Mostrar el resultado
print(f"La velocidad de Escape es {ve:.1f} [m/s]")

