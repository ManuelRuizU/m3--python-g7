
# emprendedor3.py
#ps = precio_suscripcion
#nu = numero_usuarios
#gt = gasto_total
#ua = utilidades_anterior
#uaa = utilidades_actuales
print('Actividad 2 - Rentabilidad Emprendedor III ')
print(' ')
print('¡Advertencia! El número de usuarios no puede ser negativo. Verifique los datos ingresados.')
print('¡Advertencia! Las utilidades del año anterior no pueden ser negativas. Verifique los datos ingresados. ')
print(' ')
# Solicitar datos al usuario
ps = float(input("Ingrese el precio de suscripción: "))
nu = int(input("Ingrese el número de usuarios: "))
gt = float(input("Ingrese el gasto total : "))
ua = float(input("Ingrese las utilidades del año anterior: "))

# Calcular utilidades actuales según la fórmula dada
uaa = (ps * nu) - gt

# Calcular la razón entre las utilidades actuales y las del año anterior
razon_utilidades = uaa / ua

# Mostrar resultado con dos decimales
print("La razón entre las utilidades actuales y las del año anterior es: {:.2f}".format(razon_utilidades))
print(' ')
