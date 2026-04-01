class Pato:
    def hablar(self):
        print("este pato dice cuak cuak")
    def caminar(self):
        print("Este pato esta caminando")

class Perro:
    def hablar(self):
        print("este perro dice Guau Guau")
    def caminar(self):
        print("Este perro esta caminando")

class Gato:
    def hablar(self):
        print("este gato dice Miau Miau")
    def caminar(self):
        print("Este gato esta caminando")

class Persona():
    def atrapar(self, pato):
        pato.hablar()
        pato.caminar()
        print("Lo atrapasteeeeee")

pato = Pato()
perro = Perro()
gato = Gato()
persona = Persona()

persona.atrapar(perro)

"""
# iterando entre los objetos
lista = [pato, perro, gato]
for animal in lista:
    animal.hablar()
    animal.caminar()
"""