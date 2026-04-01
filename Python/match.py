
#uso del match como un remplazo tambien del elif o switch ya que en python no existe el swtich
hora = 12

match hora:
    case 8:
        print("Hora de desayuno")
    case 13:
        print("Hora de almorzar")
    case 19:
        print("Hora de cenar")
    case _:
        print("Todavia no debes comer nada")

print("*****************************************")
#uso del match con multiple condiciones
years = 9

match years:
    case 0 | 1 | 2: print("Eres un tecnico")
    case 3 | 4: print("Eres Tecnologo")
    case 5 : print("Eres profesional")
    case 6 | 7 | 8: print("Tienes un posgrado o maestria")
    case __: print("No aplica niveles de estudio")

print("*****************************************")
#ejemplo con manejo de coordenadas puede ser utilizado
coordenada = (2, 0)
match coordenada:
    case (0, 0):
        print("Coordenada en origen")
    case (x, 0):
        print(f"Coordenada en eje x: {x}")
    case (0, y):
        print(f"Coordenada en eje y: {y}")
    case (x, y):
        print(f"Coordenada en: {x}, {y}")
    case _:
        print("Error")
