#forma no tan profesional para enumerar lista
lista = ["A", "B", "C", "D"]
indice = 0

for x in lista:
    print(f"Indice: {indice} valor: {x}")
    indice += 1

print("++++++++++++++++++++++++++++++++++++++++")
#forma mas pythonista de hacerlo o profesional
for indice, x in enumerate(lista):
    print(f"Indice: {indice:>10}| Valor: {x:>10}|")

print("++++++++++++++++++++++++++++++++++++++++")
#podemos convertir una lista en tuplas con el enumerate
mi_tupla = list(enumerate(lista))
print(mi_tupla)
