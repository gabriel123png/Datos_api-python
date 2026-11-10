ventas_iniciales = [45000, 120000, 8000, 300000]
with open("ventas.txt", "w", encoding="utf-8") as f:
    for valor in ventas_iniciales:
        f.write(str(valor) + "\n")

# 2. Leer el archivo, convertir cada línea a número y calcular el total
total_ventas = 0
with open("ventas.txt", "r", encoding="utf-8") as f:
    for linea in f:
        # .strip() elimina el salto de línea y float/int convierte el texto a número
        total_ventas += float(linea.strip())

print(f"El total de ventas es: {total_ventas}")