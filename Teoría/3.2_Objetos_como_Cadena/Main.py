from Cuenta import *
from Cliente import *
class Main:
    pass
Cuenta1 = Cuenta("Crédito",2000,"02/03/2020")
Cliente1 = Cliente("Vania", "Ciudad de México","23/05/2007",Cuenta1)
print(Cuenta1)
print(".........") #Separación entre los str de ambas clases
print(Cliente1)