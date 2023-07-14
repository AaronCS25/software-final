from fastapi import FastAPI
from datetime import datetime
from typing import List

app = FastAPI()

class Cuenta:
    def __init__(self, numero, saldo, contactos):
        self.numero = numero
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones = []

class Operacion:
    def __init__(self, numero_destino, fecha, valor):
        self.numero_destino = numero_destino
        self.fecha = fecha
        self.valor = valor

