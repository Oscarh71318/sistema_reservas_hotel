from models.habitacion import Habitacion

# crear habitaciones
h1 = Habitacion(numero=101, tipo="Doble", precio=80000,disponible=False)
h2 = Habitacion(numero=202, tipo="sencilla", precio=50000,disponible=False)

#mostrar informacion de habitaciones
h1.mostrar_info()
h2.mostrar_info()

from models.cliente import Cliente

# Crear clientes
cliente1 = Cliente("Oscar Holguin ", "713182020", "Oscar@gmail.com", "3016124433")
cliente2 = Cliente("Alberto Holguin ", "613181010", "Alberto@gmail.com", "302778800")
# muesta info clientes
cliente1.mostrar_info()
cliente2.mostrar_info()

from models.reserva import Reserva
from datetime import date

# Crear  reservas
reserva1 = Reserva(
    cliente=cliente1,
    habitacion=h1,
    fecha_inicio=date(2025, 4, 10),
    fecha_fin=date(2025, 4, 12)
)
reserva2 = Reserva(
    cliente=cliente2,
    habitacion=h2,
    fecha_inicio=date(2025, 5, 24),
    fecha_fin=date(2025, 5, 31)
)

# Mostrar información de las reservas
reserva1.mostrar_info()
reserva2.mostrar_info()

