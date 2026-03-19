from Clase_inversion import *
inversion1 = Inversion("cliente", 2000, 15)

print("Inversionista:", inversion1.inversionista)
print("Capital inicial:", inversion1.capital)
print("Tasa de interés:", inversion1.tasa_interes, "%")

años = 4
valor_final = inversion1.calcular_valor_futuro(años)
ganancia = inversion1.calcular_rendimiento(años)

print("Después de", años, "años tendrás:", round(valor_final, 2))
print("Ganancia generada:", round(ganancia, 2))

inversion1.invertir_mas(5000)

print("Nuevo capital:", inversion1.capital)

años = 4

valor_final = inversion1.calcular_valor_futuro(años)
ganancia = inversion1.calcular_rendimiento(años)

print("Nuevo valor futuro:", round(valor_final, 2))
print("Nueva ganancia:", round(ganancia, 2))

inversion1 = Inversion("Cliente", 20000, 15)