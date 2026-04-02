print(5 > 9)
print(5 < 9)
#Números complejos en python
c = 3+3j
print(c)
print(type(c))

c = 3 + 5j
print(c.real) #3.0
print(c.imag) #5.0

#También se puede crear un número complejo haciendo uso de complex, pero sin usar la j.

c = complex(3,5)
print(c) #(3+5j)

#El método strip() elimina a la izquierda y derecha el carácter que se le introduce. 
# Si se llama sin parámetros elimina los espacios. Muy útil para limpiar cadenas.
s = "   abca   "
print(s.strip()) #abc

#El método join() devuelve la primera cadena unida a cada uno de los elementos de la lista 
# que se le pasa como parámetro.

s = " y ".join(["1", "2", "3"])
print(s) #1 y 2 y 3

#El método split() divide una cadena en subcadenas y las devuelve almacenadas en una lista. 
# La división es realizada de acuerdo a el primer parámetro, y el segundo parámetro indica 
# el número máximo de divisiones a realizar.

s = "Python,Java,C"
print(s.split(",")) #['Python', 'Java', 'C']