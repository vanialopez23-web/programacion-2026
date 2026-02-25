

class Inversion:

    def __init__(self, inversionista, capital_inicial, tasa_interes):
        self.inversionista = inversionista
        self.capital = capital_inicial
        self.tasa_interes = tasa_interes

    def invertir_mas(self, cantidad):
        self.capital += cantidad
        print("Se agregaron $", cantidad)

    def calcular_valor_futuro(self, años):
        tasa_decimal = self.tasa_interes / 100
        return self.capital * (1 + tasa_decimal) ** años

    def calcular_rendimiento(self, años):
        return self.calcular_valor_futuro(años) - self.capital

inversion1 = Inversion("Cliente", 20000, 15)

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

# Crear inversión con datos del usuario
nombre = input("Ingresa el nombre del inversionista: ")
capital = float(input("Ingresa el capital inicial: "))
tasa = float(input("Ingresa la tasa de interés anual (%): "))

inversion1 = Inversion(nombre, capital, tasa)

while True:
    print("\n----- MENÚ -----")
    print("1. Invertir más dinero")
    print("2. Calcular valor futuro")
    print("3. Calcular rendimiento")
    print("4. Mostrar datos actuales")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        cantidad = float(input("¿Cuánto deseas agregar? "))
        inversion1.invertir_mas(cantidad)

    elif opcion == "2":
        años = int(input("¿Cuántos años? "))
        valor = inversion1.calcular_valor_futuro(años)
        print("Valor futuro:", round(valor, 2))

    elif opcion == "3":
        años = int(input("¿Cuántos años? "))
        ganancia = inversion1.calcular_rendimiento(años)
        print("Rendimiento:", round(ganancia, 2))

    elif opcion == "4":
        print("Inversionista:", inversion1.inversionista)
        print("Capital actual:", inversion1.capital)
        print("Tasa de interés:", inversion1.tasa_interes, "%")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intenta de nuevo.")
