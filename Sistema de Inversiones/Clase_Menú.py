# Crear inversión con datos del usuario
from Clase_inversion import *
from Cliente import *

nombre = input("Ingresa el nombre del cliente: ")
edad = int(input("Ingresa la edad: "))
fecha_nacimiento = input("Ingresa la fecha de nacimiento: ")

capital = float(input("Ingresa el capital inicial: "))
tasa = float(input("Ingresa la tasa de interés anual (%): "))

cliente1 = Cliente(nombre, edad, fecha_nacimiento)
inversion1 = Inversion(cliente1, capital, tasa)

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