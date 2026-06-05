class Cuenta:
    def __init__(self, numero_cuenta, saldo_inicial=0.0):
        self._numero_cuenta = numero_cuenta  # Atributo protegido para herencia
        self._saldo = float(saldo_inicial)   # Atributo protegido

    def get_saldo(self):
        return self._saldo

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            return True
        return False

    def pagar_compra(self, monto):
        if self._saldo >= monto:
            self._saldo -= monto
            return True
        return False

    def __str__(self):
        return f"Cuenta Nro: {self._numero_cuenta} | Saldo: ${self._saldo:.2f}"
