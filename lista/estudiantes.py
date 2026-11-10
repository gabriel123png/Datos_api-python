estudiantes = ["Carlos", "Ana", "Luis"]

# 1. Guardar los nombres en el archivo (uno por línea)
with open("estudiantes.txt", "w", encoding="utf-8") as f:
    for nombre in estudiantes:
        f.write(nombre + "\n")

# 2. Leer el archivo e imprimir cada nombre numerado
with open("estudiantes.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        print(f"{i} {linea.strip()}")

with open("estudiantes.txt", "a", encoding="utf-8") as f:
    f.write("Marta\n")

# 2. Leer el archivo, contar las líneas y mostrar el total
with open("estudiantes.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    total_estudiantes = len(lineas)

print(f"Número total de estudiantes: {total_estudiantes}")