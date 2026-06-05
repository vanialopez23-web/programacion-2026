class Cliente:
    def __init__(self, cedula, nombre, telefono):
        self.__cedula = cedula          # Atributo privado
        self.__nombre = nombre          # Atributo privado
        self.telefono = telefono        # Atributo público
        self.cuentas = {}               # Relación: Diccionario para almacenar objetos Cuenta

    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula

    def agregar_cuenta(self, tipo_cuenta, objeto_cuenta):
        self.cuentas[tipo_cuenta] = objeto_cuenta

    def __str__(self):
        return f"Cliente: {self.__nombre} | Cedula: {self.__cedula} | Telefono: {self.telefono}"
