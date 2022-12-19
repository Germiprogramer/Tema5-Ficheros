from datetime import datetime

class Reloj:

    def __init__(self, hora, minutos, segundos):
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos

    def __str__(self):
        return f"{self.hora}:{self.minutos}:{self.segundos}"


dt = datetime.now()

reloj = Reloj(dt.hour, dt.minute, dt.second)

print(reloj)