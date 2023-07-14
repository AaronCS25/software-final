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
    def __init__(self, numero_origen, numero_destino, fecha, valor):
        self.numero_origen = numero_origen
        self.numero_destino = numero_destino
        self.fecha = fecha
        self.valor = valor

# List<Cuenta> BD = new List<Cuenta>();
BD = []
BD.append(Cuenta("21345", "Arnaldo", 200, ["123", "456"]))
BD.append(Cuenta("123", "Luisa", 400, ["456"]))
BD.append(Cuenta("456", "Andrea", 300, ["21345"]))

# Functions
def buscar_dueno(numero_de_cuenta):
    for cuenta in BD:
        if cuenta.numero == numero_de_cuenta:
            return cuenta.dueno

# Endpoints
@app.get("/")
def home():
    return "Everything is working!"

@app.get("/billetera/contactos")
def obtener_contactos(minumero: str):
    for cuenta in BD:
        if cuenta.numero == minumero:
            contactos = {}
            for contacto_numero in cuenta.contactos:
                contacto_dueno = buscar_dueno(contacto_numero)
                contactos[contacto_numero] = contacto_dueno
            return contactos

    return {"mensaje": "No se encontró la cuenta"}

@app.post("/billetera/pagar")
def pagar(minumero: str, numerodestino: str, valor: int):
    cuenta_origen = None
    cuenta_destino = None

    for cuenta in BD:
        if cuenta.numero == minumero:
            cuenta_origen = cuenta
        elif cuenta.numero == numerodestino:
            cuenta_destino = cuenta
    
    if cuenta_origen is None:
        return {"mensaje": "No se encontró la cuenta origen"}
    
    if cuenta_destino is None:
        return {"mensaje": "No se encontró la cuenta destino"}
    
    if cuenta_origen.saldo < valor:
        return {"mensaje": "No tiene saldo suficiente"}
    
    cuenta_origen.saldo -= valor
    cuenta_destino.saldo += valor

    fecha = datetime.now()
    operacion = Operacion(minumero, numerodestino, fecha, valor)
    cuenta_origen.operaciones.append(operacion)
    cuenta_destino.operaciones.append(operacion)

    return {"mensaje": "Pago exitoso", "fecha": f"Realizado en {fecha}"}

@app.get("/billetera/historial")
def get_historial(minumero: str):
    for cuenta in BD:
        if cuenta.numero == minumero:
            if cuenta.operaciones == []:
                return {"mensaje": "No hay operaciones"}
            
            historial = []
            saldo_actual = cuenta.saldo
            historial.append(f'Saldo de {cuenta.dueno}: {saldo_actual}')
            historial.append(f'Operaciones de {cuenta.dueno}:')

            for operacion in cuenta.operaciones:
                if operacion.numero_origen == minumero:
                    tipo_operacion = 'Pago realizado'
                    detalle_operacion = f'a {buscar_dueno(operacion.numero_destino)}'
                    monto_operacion = operacion.valor
                else:
                    tipo_operacion = 'Pago recibido'
                    detalle_operacion = f'de {buscar_dueno(operacion.numero_origen)}'
                    monto_operacion = operacion.valor
                
                fecha_operacion = operacion.fecha.strftime("%d/%m/%Y %H:%M:%S")
                historial.append(f'{tipo_operacion} {detalle_operacion} por {monto_operacion} el {fecha_operacion}')
            return historial
        
    return {"mensaje": "No se encontró la cuenta"}