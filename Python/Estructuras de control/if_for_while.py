#el Switch en python no existe pero se remplaza con el if, elif y else
import time
edad = int(input("Elije una opción para saber tu rango de edad: "))

if edad > 0 and edad < 8:
    print("Eres un niño feliz")
elif edad > 7 and  edad < 13:
    print("Eres un pre-adolescente")
elif edad > 12 and edad < 18:
    print("Eres un adolescente")
elif edad > 17 and edad < 20:
    print("Estas en una edad entrando a la adultes")
elif edad > 19 and edad < 62:
    print("Estas en una edad adulta")
elif edad > 61 and edad < 95:
    print("Estas en una edad de vejez")
else:
    print("Tu edad no esta entre los limites de longevidad")

print("***************************************************************")

my_name = "CAMILO"
for x in my_name:
    print(x)


lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for x in lista:
    print(x)

for x in lista:
    for j in x:
        print(j)

print("***************************************************************")
#range
my_list = list(range(10,21,2))
print(my_list)
my_list2 = list(range(20, 9, -2))
print(my_list2)

print("***************************************************************")
#while
list_numeros = ["uno", "dos", "tres", "cuatro"]
while list_numeros:
    list_numeros.pop(0)
    print(list_numeros)
else:
    print("Se eliminaron todos los valores de la lista")

#otro ejemplo 
x1 = 10
mi_recta_num = []
while True:
    x1 -=1
    print(x1)
    mi_recta_num.append(x1)
    if x1 <= -9:
        break
else:
    print("fin del listado")
print(mi_recta_num)

#while anidado
#ejemplo con permutación de números buscando las posibles combinaciones de los números

i = 0
j = 0
contador = 0
while i < 3:
    while j < 3:
        print(i,j)
        j+= 1
        contador+= 1
    i+=1
    j=0
print(f"Tienes un total de {contador} combinaciones posibles")

#arbol con * utilizando while

a = 12
b = 1
t = 4
t2 = a-3

print(" " * a + "🔴" * b)
while a > 0:
    time.sleep(1)
    print(" " * a + "*" * b)
    a-= 1
    b+= 2

while t > 0:
    time.sleep(1)
    print(" " * t2 + "|  🟫  |")
    t-= 1

