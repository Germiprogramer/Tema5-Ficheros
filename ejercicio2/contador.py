import pickle
import os

def crearFichero():
    try:
        fichero = open('ejercicio2/contador.txt','r')
        fichero.close()
    except:
        fichero = open('ejercicio2/contador.txt','w')
        fichero.write("0")
        fichero.close()

def leerFichero():
    fichero = open('ejercicio2/contador.txt','r')
    contador = fichero.read()
    fichero.close()
    return contador

def escribirFichero(argumento):
    if argumento == "inc":
        contador = leerFichero()
        fichero = open('ejercicio2/contador.txt','w')
        fichero.write(str(1+ int(contador)))
        fichero.close()
        print("El valor del fichero es: {}".format(leerFichero()))
    elif argumento == "dec":
        contador = leerFichero()
        fichero = open('ejercicio2/contador.txt','w')
        fichero.write(str(-1 + int(contador)))
        fichero.close()
        print("El valor del fichero es: {}".format(leerFichero()))
    else:
        print("El valor del fichero es: {}".format(leerFichero()))

#prueba del codigo
crearFichero()
escribirFichero("inc")
escribirFichero("inc")
escribirFichero("in")


