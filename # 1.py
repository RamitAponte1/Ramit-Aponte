# 1. Acceso básico
lista_1 = [100, 200, 300, 400]
primero = lista_1[0]
ultimo = lista_1[-1]

print("--- Acceso básico ---")
print(f"Primer elemento: {primero}")  # Salida: 100
print(f"Último elemento: {ultimo}")    # Salida: 400

# 2. Listas anidadas
lista_2 = [50, True, "datos", [7, 8]]
valor = lista_2[3][1]

print("\n--- Listas anidadas ---")
print(f"Valor extraído: {valor}")  # Salida: 8

# 3. Longitud de la lista
n = len(lista_1)

print("\n--- Longitud ---")
print(f"Total de elementos en lista_1: {n}")  # Salida: 4