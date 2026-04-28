from src.models.service import Service


class RoomReservation(Service):

    def calculate_cost(self, hours=1):
        return self.base_price * hours

    def description(self):
        return f"Room reservation service: {self.name}"