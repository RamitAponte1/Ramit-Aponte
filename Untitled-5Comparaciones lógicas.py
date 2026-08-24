# Descripción: Evalúa tres condiciones booleanas entre dos edades

# 1. Definir las dos edades
edad1 = 20
edad2 = 18

# 2. Evaluar condiciones
son_iguales = edad1 == edad2
primera_es_mayor = edad1 > edad2
ambas_mayores_18 = (edad1 >= 18) and (edad2 >= 18)

# 3. Imprimir los booleanos
print("¿Son iguales?:", son_iguales)
print("¿La primera es mayor?:", primera_es_mayor)
print("¿Ambas son mayores de edad (>=18)?:", ambas_mayores_18)