#asignar valores a las variales
e, f, g, h = range(1,5)

print(e, f, g, h)

a = 10
b: int = 20

print(f"10 x 20 = {a*b}")
c = a*b

if c == 200:
    print(f"Excelente el resultado es: {c}")
elif c == 150:
    print(f"No fue el resultado esperado, el resultado es: {c}")
else:
    print(f"Wow no esperabamos esto, el resultado es: {c}")

mi_texto = "Hola Camilo"

print(mi_texto)

x = 0

while(x <= b):
    if x == 10 or x == 15:
        x+=1
        continue 
    
    else:
        print(x)
        x+= 1


nombre = list("camilo")
print(nombre)

print("************************************************+")

def pares(limite):
    lista = []
    for x in range(limite+1):
        if (x % 2) == 0:
            lista.append(x)
    return lista

def impares(limite):
    lista = []
    for x in range(limite+1):
        if (x % 2) == 1:
            lista.append(x)
    return lista

valor_calcular = 20

print(pares(valor_calcular))
print(impares(valor_calcular))

print("*************************************************")

def valor_a_buscar(valor_buscar):

    valor_list = pares(valor_calcular)
    if valor_buscar in valor_list:
        print(f"El valor buscado {valor_buscar}, fue encontrado con exito")
    else:
        print(f"El valor buscado {valor_buscar}, no fue encontrado")


print(valor_a_buscar(20))
