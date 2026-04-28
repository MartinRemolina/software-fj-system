from src.exceptions.custom_exceptions import ReservationError


class Reservation:

    def __init__(self, client, service, duration):
        if duration <= 0:
            raise ReservationError("Duration must be greater than 0")

        self.client = client
        self.service = service
        self.duration = duration
        self.status = "Pending"

    def confirm(self):
        self.status = "Confirmed"

    def cancel(self):
        self.status = "Cancelled"

    def process(self):
        try:
            cost = self.service.calculate_cost(self.duration)
            self.confirm()
            return f"Reservation confirmed. Total cost: {cost}"

        except Exception as e:
            raise ReservationError("Error processing reservation") from e