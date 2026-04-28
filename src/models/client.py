from src.exceptions.custom_exceptions import InvalidDataError


class Client:
    """
    Represents a system client with basic validation.
    """

    def __init__(self, name, email):
        if not name:
            raise InvalidDataError("Name cannot be empty")

        if "@" not in email:
            raise InvalidDataError("Invalid email format")

        self.__name = name
        self.__email = email

    def get_info(self):
        return f"Client: {self.__name}, Email: {self.__email}"