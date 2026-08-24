# Descripción: Verifica si un número es par o impar usando el operador %

# 1. Definir el número a evaluar
numero = 7

# 2. Calcular el residuo al dividir entre 2
# Si el residuo es 0 es par, de lo contrario es impar
es_par = (numero % 2 == 0)

# 3. Mostrar el resultado
print("El número es:", numero)
print("¿Es par?:", es_par)