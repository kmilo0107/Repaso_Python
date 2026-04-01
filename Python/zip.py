# Es una función que permite recorrer varias listas (o iterables) al mismo tiempo
#Une elementos por posición

nombres = ["Camilo", "Sara", "Carolina", "Pilar"]
edades = [38, 6, 35, 61]

for nombre, edad in zip(nombres,edades):
    print(f"mi nombre es: {nombre} y tengo {edad} años")

print("****************************************************")
# crea pares como tuplas
# si tiene una lista más corta lo hara hasta la lista más corta
print("\nimpresión en lista muestra que convierte en tuplas")
print(list(zip(nombres, edades)))
z = zip(nombres, edades)

print("****************************************************")
# Creando diccionarios
claves = ["nombre", "edad"]
valores = ["Juan", 30]

dic = dict(zip(claves, valores))
print(dic)
print(dic.items)
print("****************************************************")
#separando valores (Unzip)
pares = [("a", 1), ("b", 2)]

letras, numeros = zip(*pares)

print(letras)   # ('a', 'b')
print(numeros)  # (1, 2)


print("****************************************************")
# EJERCICIOS CON ZIP

productos = ["Laptop", "Mouse", "Teclado"]
precios = [2000, 50, 100]

for p, precio in zip(productos, precios):
    print(f"{p}: ${precio}")

print("****************************************************")

productos = ["Laptop", "Mouse", "Teclado"]
cantidades = [5,10,10]
precios = [2000, 50, 100]

for p, cant, precio in zip(productos, cantidades, precios):
    print(f"{p}: cantidad: {cant}: ${precio}")

print("****************************************************")

#ejercicio sumando listas
resultado = []
a = [5, 10, 9]
b = [15, 5, 13]

for v1, v2 in zip(a,b):
    resultado.append(v1 + v2)
print(resultado)

print("****************************************************")
#Comparar dos listas y guardar el mayor de cada posición
a2 = [5, 8, 2]
b2 = [3, 10, 4]
mayora = a2[0]
mayorb = b2[0]
resultado2 = []
for v1, v2 in zip(a2, b2):
    if v1 > mayora:
        mayora = v1
    if v2 > mayorb:
        mayorb = v2
resultado2.append(mayora)
resultado2.append(mayorb)
print("COMPARANDO LISTAS")
print(f"El número mayor de cada lista es: {resultado2}")

print("****************************************************")
#Segunda forma de realizarlo más corta

resultado = []

resultado.append(max(a2))
resultado.append(max(b2))

print(f"El resultado mayor con fun max es: {resultado}")

print("****************************************************")
nombres = ["Ana", "Luis", "Pedro"]
edades = [20, 25, 30]

mydiccionary = dict(zip(nombres, edades))
print(mydiccionary)
print("****************************************************")
#Mostrar solo los que aprobaron (nota ≥ 3)

estudiantes = ["Ana", "Luis", "Pedro"]
notas = [2.5, 3.8, 3.2]

apronotas = []
aproestudiantes = []
for x, y in zip(estudiantes,  notas):
    if y > 2.9:
        apronotas.append(y)
        aproestudiantes.append(x)

totalresult = dict(zip(aproestudiantes,apronotas))
print(f"Estudiantes que aprobaron: {totalresult}")
print("****************************************************")

#multiplicación tipo matriz
a = [1, 2, 3]
b = [4, 5, 9]

resultadomulti = []

for v1, v2 in zip(a,b):
    resultadomulti.append(v1*v2)
print(f"El resultado de multiplicar listas es : {resultadomulti}")
print("****************************************************")
#El mismo resultado pero menos lineas
resulmulti = [v1*v2 for v1, v2 in zip(a,b)]
print(f"El resultado es:::: {resulmulti}")


print("****************************************************")
#ejercicio <10 es formateo de python < es alineación izquierda
productos = ["Laptop", "Mouse", "Teclado"]
precios = [2000, 50, 100]
stock = [5, 10, 3]

for producto, precio, disponible in zip(productos, precios, stock):
    print(f"{producto:<10} | Precio: ${precio:<5} | Stock: {disponible}")

print("****************************************************")
stock_menor_seis = []
for producto, precio, disponible in zip(productos, precios, stock):
    if disponible < 6:
        stock_menor_seis.append(producto)
print(f"productos con stock menor a 6: {stock_menor_seis}")


print("****************************************************")
stock_menor_seis = [producto for producto, _, disponible in zip(productos, precios, stock) if disponible < 6]
print(f"Productos con stock menor a 6: {stock_menor_seis}")
print("****************************************************")