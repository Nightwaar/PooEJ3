datos = [
    ["Juan", 25, "Hombre"],
    ["María", 32, "Mujer"],
    ["Pedro", 45, "Hombre"],
    ["Lucía", 28, "Mujer"],
]

# Encabezado de la tabla
encabezado = ["Nombre", "Edad", "Género"]

# Imprimir el encabezado de la tabla
print("|".join(encabezado))

# Imprimir una línea separadora
print("-" * 20)

# Imprimir los datos de la tabla
for fila in datos:
    # Crear una cadena de formato con tres columnas, con alineamiento a la izquierda, derecha e izquierda respectivamente
    formato = "{:<10}|{:>5}|{:>10}"
    # Aplicar la cadena de formato a cada elemento de la fila y unirlos con el separador "|"
    fila_formateada = formato.format(*fila)
    # Imprimir la fila formateada
    print(fila_formateada)