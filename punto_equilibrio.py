def punto_equilibrio(f, s, v):
    return f / (s - v)

def ganancia(s, v, x, f):
    return (s - v) * x - f

# Ingreso de valores por teclado
s = float(input("Ingresa el precio de venta por unidad (s): "))
f = float(input("Ingresa el costo fijo (f): "))
v = float(input("Ingresa la venta/costo variable (v): "))
x = float(input("Ingresa el número de unidades vendidas (x): "))

# Resultados
pe = punto_equilibrio(f, s, v)
gan = ganancia(s, v, x, f)

print("\n--- RESULTADOS ---")
print(f"Punto de equilibrio: {pe} unidades")
print(f"Ganancia: {gan}")
