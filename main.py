from fastapi import FastAPI
from datetime import datetime
from typing import List

app = FastAPI()

# Classes
class Cuenta:
    def __init__(self, numero, dueno, saldo, contactos):
        self.numero = numero
        self.dueno = dueno
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones = []

class Operacion:
    def __init__(self, numero_destino, fecha, valor):
        self.numero_destino = numero_destino
        self.fecha = fecha
        self.valor = valor

#List<Cuenta> BD = new List<Cuenta>();
BD = []
BD.append(Cuenta("21345", "Arnaldo", 200, ["123", "456"]))
BD.append(Cuenta("123", "Luisa", 400, ["456"]))
BD.append(Cuenta("456", "Andrea", 300, ["21345"]))