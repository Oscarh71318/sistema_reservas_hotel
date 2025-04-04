class Cliente:
    def __init__(self, nombre, documento, correo, telefono):
        self.nombre = nombre
        self.documento = documento  # Ej: número de cédula o pasaporte
        self.correo = correo
        self.telefono = telefono

    def mostrar_info(self):

        print(f"Cliente: {self.nombre} | Documento: {self.documento} | Correo: {self.correo} | Teléfono: {self.telefono}")
