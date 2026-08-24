# Lista inicial
l = [5, 10, 15]
print(f"Lista inicial: {l}")

# --- Modificar y Agregar ---
l[1] = 99
print(f"Después de l[1] = 99: {l}")

l.append(20)
print(f"Después de append(20): {l}")

l.insert(1, 44)
print(f"Después de insert(1, 44): {l}")

l.extend([30, 40])
print(f"Después de extend([30, 40]): {l}")

# --- Eliminar ---
l.remove(44)
print(f"Después de remove(44): {l}")

x = l.pop()
print(f"Elemento extraído con pop(): {x}")
print(f"Lista después de pop(): {l}")

l[1:3] = [100, 200, 300]
print(f"Después de reemplazar slice l[1:3]: {l}")