from Cliente import Cliente
from Cuenta_ahorro import CuentaAhorro
from Cuenta_credito import CuentaCredito
from Menu import CarritoCompras

def ejecutar_sistema():
    print("=== CONFIGURACION INICIAL DEL CLIENTE ===")
    nombre = input("Nombre del cliente: ")
    cedula = input("Cedula: ")
    telefono = input("Telefono: ")
    
    cliente = Cliente(cedula, nombre, telefono)
    
    cuenta_ahorro = CuentaAhorro(numero_cuenta="AH-101", saldo_inicial=500.0)
    cuenta_credito = CuentaCredito(numero_cuenta="CR-202", limite_credito=1200.0)
    
    cliente.agregar_cuenta("ahorro", cuenta_ahorro)
    cliente.agregar_cuenta("credito", cuenta_credito)
    
    carrito = CarritoCompras()
    
    while True:
        print("\n" + "="*40)
        print(f" SISTEMA DE COMPRAS EN LINEA - USUARIO: {cliente.get_nombre().upper()} ")
        print("="*40)
        print("1. Ver perfil y estados de cuenta")
        print("2. Realizar una compra")
        print("3. Depositar en Cuenta de Ahorros")
        print("4. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            print("\n--- INFORMACION DEL CLIENTE ---")
            print(cliente)
            print(cliente.cuentas["ahorro"])
            print(cliente.cuentas["credito"])
            
        elif opcion == "2":
            carrito.vaciar_carrito()
            while True:
                carrito.mostrar_catalogo()
                print("[0] Finalizar seleccion de productos")
                try:
                    prod_opcion = int(input("Seleccione el codigo del producto: "))
                    if prod_opcion == 0:
                        break
                    carrito.agregar_al_carrito(prod_opcion)
                except ValueError:
                    print("Por favor, ingrese un numero valido.")
            
            total_compra = carrito.calcular_total()
            if total_compra == 0:
                print("No selecciono ningun producto.")
                continue
                
            print(f"\nTotal de la compra: ${total_compra:.2f}")
            print("Metodos de pago:")
            print("1. Cuenta de Ahorros")
            print("2. Tarjeta de Credito")
            print("3. Cancelar operacion")
            
            metodo_pago = input("Seleccione metodo de pago: ")
            
            if metodo_pago == "1":
                if cliente.cuentas["ahorro"].pagar_compra(total_compra):
                    print("Operacion exitosa: Pago realizado con Cuenta de Ahorros.")
                else:
                    print("Error: Fondos insuficientes en la cuenta de ahorros.")
                    
            elif metodo_pago == "2":
                if cliente.cuentas["credito"].pagar_compra(total_compra):
                    print("Operacion exitosa: Cargo aprobado en Tarjeta de Credito.")
                else:
                    print("Error: El monto supera el limite de credito disponible.")
            else:
                print("Compra cancelada.")
                
        elif opcion == "3":
            try:
                monto_dep = float(input("Monto a depositar en ahorros: $"))
                if cliente.cuentas["ahorro"].depositar(monto_dep):
                    print("Operacion exitosa: Deposito procesado.")
                else:
                    print("Error: Monto invalido.")
            except ValueError:
                print("Error: Entrada invalida.")
                
        elif opcion == "4":
            print("Finalizando el programa.")
            break
        else:
            print("Opcion invalida, intente nuevamente.")

if __name__ == "__main__":
    ejecutar_sistema()
