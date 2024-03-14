
# emprendedor2.py
#psn = precio suscripcion norma
#psp = precio suscripcion premium
#nun = numero usuarios normal
#nup = numero usuarios premium
#gt = gasto tota
#it = ingresos totales
print(' ')
print('Actividad 2 - Rentabilidad Emprendedor II ')
print(' ')
# Solicitar datos al usuario
psn = float(input("Ingrese el precio de suscripción para usuarios normales : "))
psp = float(input("Ingrese el precio de suscripción para usuarios premium : "))
nun = int(input("Ingrese el número de usuarios normales : "))
nup = int(input("Ingrese el número de usuarios premium : "))
gt = float(input("Ingrese el gasto total (GT): "))

# Calcular ingresos totales
it = (psn * nun) + (psp * nup)

# Calcular utilidades según la fórmula dada
utilidades = it - gt

# Mostrar resultado
print("Las utilidades del proyecto son:", utilidades)
print(' ')
