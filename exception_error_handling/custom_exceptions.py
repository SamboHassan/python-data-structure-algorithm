class CustomError(Exception):
    """Base class for other exceptions"""

    pass


class InputError(CustomError):
    """Raised when the input value is not as expected"""

    pass


class CalculationError(CustomError):
    """Raised when an error occurs during a calculation"""

    pass
