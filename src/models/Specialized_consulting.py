from src.models.service import Service 

class SpecializedConsulting(Service):
    def __init__(self, name,base_price, expert_level="Senior"):
        supper().__init__(name, base_price)
        self.expert_level = expert_level 

    def calculate_cost(self, hours, discount=0,tax=0.19):
        """
        Metodo Sobrecargo:
        Permmite calcular el costo base, o incluir un descuento 
        y un impuesto opcional.
        """
        subtotal = self.base_price * hours 
        total_with_discount = subtotal - (subtotal * discount) 
        total = total_with_discount * (1 + tax)
        return round(total, 2)

    def description(self):
        return f"Asesoria Especializada ({self.expert_level}): {self.name}"
