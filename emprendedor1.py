
# emprendedor1.py
#ps = precio de la supcripcion
#nu = numero de usuarios
#gt = gasto total

print(' ')
print('Actividad 2 - Rentabilidad ')
print(' ')
# Solicitar datos al usuario
ps = float(input("Ingrese el precio de suscripción (P): "))
nu = int(input("Ingrese el número de usuarios (U): "))
gt = float(input("Ingrese el gasto total (GT): "))

# Calcular utilidades según la fórmula dada
utilidades = (ps * nu) - gt

# Mostrar resultado
print("Las utilidades del proyecto son:", utilidades)
print(' ')
