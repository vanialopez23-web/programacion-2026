# Cuenta_ahorro.py
from Cuenta import Cuenta

class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta, saldo_inicial=0.0, interes=0.02):
        super().__init__(numero_cuenta, saldo_inicial)
        self.interes = interes

    def aplicar_interes(self):
        self._saldo += self._saldo * self.interes


# Cuenta_credito.py
from Cuenta import Cuenta

class CuentaCredito(Cuenta):
    def __init__(self, numero_cuenta, limite_credito=1000.0):
        super().__init__(numero_cuenta, saldo_inicial=limite_credito)
        self.limite_credito = limite_credito
        self.deuda = 0.0

    def pagar_compra(self, monto):
        if (self.limite_credito - self.deuda) >= monto:
            self.deuda += monto
            self._saldo -= monto
            return True
        return False

    def __str__(self):
        return f"Credito Nro: {self._numero_cuenta} | Disponible: ${self._saldo:.2f} | Deuda: ${self.deuda:.2f}"
