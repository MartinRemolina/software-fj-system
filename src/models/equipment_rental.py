from src.models.service import Service 

#class EquipmentRental(Service):
#  def __init__(self,namr, base_price, insurance_fee=15.0):
#    # pasamos el nombre y precio base a clase padre (service) 
#    super().__init__(name,base_price)
#    # Añadimos un atributo unico para el servicio : seguro 
#    self.insurance_fee = insurance_fee
#
#  def calculate_cost(self, duration):
#    """
#    sobreescritura (poliformismo):
#    costo = (precio base * duracion) + seguro fijo 
#    """
#
#    return (self.base_price * duration) + self.insurance_fee
#
# def description(self):
#     return f"Alquiler de Equipo: {self.name} (incluye seguro de {self.insurance_fee})"

#from src.models.service import Service


class EquipmentRental(Service):

    def calculate_cost(self, duration=1):

        return self.base_price * duration

    def description(self):

        return f"Equipment rental service: {self.name}"


