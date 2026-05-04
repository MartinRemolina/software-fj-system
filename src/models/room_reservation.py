from src.models.service import Service
from src.exceptions.custom_exceptions import InvalidDataError


class RoomReservation(Service):
    """
    Concrete service that represents a room reservation.

    This service calculates the total cost based on the number of hours
    and validates that the input parameters are correct.
    """

    def calculate_cost(self, hours=1):
        """
        Calculates the cost of the reservation.

        :param hours: Number of hours for the reservation
        :return: Total cost
        :raises InvalidDataError: If hours is invalid
        """

        if hours <= 0:
            raise InvalidDataError("Hours must be greater than 0")

        return self.base_price * hours

    def description(self):
        """
        Returns a description of the service.

        :return: String description
        """
        return f"Room reservation service: {self.name}"