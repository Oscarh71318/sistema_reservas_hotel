from models.habitacion import Habitacion


h1 = Habitacion(numero=101, tipo="Doble", precio=80.000,disponible=True)
h2 = Habitacion(numero=202, tipo="sencilla", precio=50.000,disponible=False)

h1.mostrar_info()
h2.mostrar_info()

from models.cliente import Cliente

# Crear un cliente
cliente1 = Cliente("Oscar Holguin ", "713182020", "Oscar@gmail.com", "3016124433")

# muesta info cliente
cliente1.mostrar_info()
