#ejemplo para crear la lista de los cuadrado de los primeros x números
print([x ** 2 for x in range(5) ])
print("****************************************************")

#puedo usar el mismo ejemplo y crear una lista
my_lista = []
for x in range(5):
    my_lista.append(x ** 2 )
print(my_lista)
print("****************************************************")

#el mismo ejemplo anterior más corto y profesional
my_lista2 = [x ** 2 for x in range(5)]
print(my_lista2)
print("****************************************************")

#llamando una función también se puede usar
def cuadrado_num(num):
    return num ** 2
my_lista3 = [cuadrado_num(x) for x in range(5)]
print(my_lista3)
print("****************************************************")

#ejemplo, podemos dividir los númros de un listado
lista = [10, 20, 30, 40, 50]
nueva_lista = [x/10 for x in lista]
print(nueva_lista)
print("****************************************************")

#PODEMOS REALIZAR AÑADIENDO CONDICIONALES
# lista = [expresión for elemento in iterable if condición]
#ejemplo con condicional
frase = "El perro de san roque no tiene rabo"
mis_letras = [x for x in frase if x == "r"]
print(mis_letras)
print(f"La letra r se repite {mis_letras.count("r")} veces")
print(len(mis_letras))
print("****************************************************")
#Sets comprehension
#La única diferencia es que debemos cambiar el () por {}. Como resulta evidente, 
# dado que los set no permiten duplicados, si intentamos añadir un elemento que 
# ya existe en el set, simplemente no se añadirá.
frase = "El perro de san roque no tiene rabo"
mi_set = {i for i in frase if i == "r"}
print(mi_set)
