from datetime import date

class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def mostrar_info(self):
        print("=== RESERVA ===")
        self.cliente.mostrar_info()
        self.habitacion.mostrar_info()
        print(f"Desde: {self.fecha_inicio} Hasta: {self.fecha_fin}")
