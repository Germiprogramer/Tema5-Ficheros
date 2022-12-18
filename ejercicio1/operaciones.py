def suma(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Tipo de dato no valido"
    return a + b

def resta(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Tipo de dato no valido"
    return a - b

def multiplicacion(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Tipo de dato no valido"
    return a * b

def division(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Tipo de dato no valido"
    try: 
       return a / b
    except ZeroDivisionError:
        return "No se puede dividir por 0"


