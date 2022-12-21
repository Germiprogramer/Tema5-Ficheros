import pickle
import os

class Personaje:

    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return f"Nombre: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque}, Defensa: {self.defensa}, Alcance: {self.alcance}"
    
#crear una clase gestor que tenga un metodo que guarde un personaje en un fichero

class Gestor:

    def __init__(self):
        pass

    def guardarPersonaje(self, personaje):
        fichero = open('ejercicio3/personaje.pckl', 'wb')
        pickle.dump(personaje, fichero)
        fichero.close()

#crear una clase gestor que tenga un metodo que mostrar un personaje de un fichero

    def mostrarPersonaje(self):
        fichero = open('ejercicio3/personaje.pckl', 'rb')
        personaje = pickle.load(fichero)
        fichero.close()
        return personaje
    
#crear una clase gestor que tenga un metodo que borre un personaje de un fichero

    def borrarPersonaje(self):
        os.remove('ejercicio3/personaje.pckl')

#prueba del codigo

caballero = Personaje("caballero", 4, 2, 4, 2)
guerrero = Personaje("guerrero", 2, 4, 2, 4)
arquero = Personaje("arquero", 2, 4, 1, 8)

gestor = Gestor()

gestor.guardarPersonaje(caballero)
gestor.guardarPersonaje(guerrero)
gestor.guardarPersonaje(arquero)

print(gestor.mostrarPersonaje())
    


    