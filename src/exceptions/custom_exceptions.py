class InvalidDataError(Exception):
    """Raised when input data is invalid"""
    pass


class ServiceNotAvailableError(Exception):
    """Raised when a service is not available"""
    pass


class ReservationError(Exception):
    """General reservation error"""
    pass

