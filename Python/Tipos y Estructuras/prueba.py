edades = [38, 35, 6, 61]
nombres = ["Camilo", "Carolina", "Sara", "Pilar"]

for x, y in zip(edades, nombres):
    print(f"| Mi nombre es {y:<10} y tengo {x:<5} años |")

print(edades)

edades += nombres
print(edades.index("Pilar"))
print(edades)
edades.reverse()
print(edades)
print(edades.index("Pilar"))