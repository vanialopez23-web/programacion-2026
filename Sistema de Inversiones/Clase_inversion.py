'''
created by vania@ciencias.unam.mx
'''

#Clase para la identificación de las inversiones del programa
class Inversion:

    def __init__(self, inversionista, capital_inicial, tasa_interes):
        self.inversionista = inversionista
        self.capital = float(capital_inicial)
        self.tasa_interes = tasa_interes

    def invertir_mas(self, cantidad):
        self.capital += cantidad
        print("Se agregaron $", cantidad)

    def calcular_valor_futuro(self, años):
        tasa_decimal = self.tasa_interes / 100
        return self.capital * (1 + tasa_decimal) ** años

    def calcular_rendimiento(self, años):
        return self.calcular_valor_futuro(años) - self.capital