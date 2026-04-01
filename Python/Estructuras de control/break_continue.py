#uso del break, en este caso romple todo el ciclo
for z in range(1,10):
    if z == 8:
        break
    print(z, end=" ")

print("\n******************************")
#uso del continue, en este caso al cumplir la condición salta el ciclo 
y = 0
while y < 10:
    y+= 1
    if y == 6:
        continue
    print(y, end=" ")   
    