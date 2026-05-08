from src.models.service import Service


class ConsultingService(Service):

    def calculate_cost(self, duration=1):

        return self.base_price * duration * 1.2

    def description(self):

        return f"Consulting service: {self.name}"