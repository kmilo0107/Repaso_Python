lista = ["A", "B", "C", "D"]
indice = 0

for x in lista:
    print(f"Indice: {indice} valor: {x}")
    indice += 1

print("++++++++++++++++++++++++++++++++++++++++")

for indice, x in enumerate(lista):
    print(f"Indice: {indice:>10}| Valor: {x:>10}|")