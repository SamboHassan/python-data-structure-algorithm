from custom_exceptions import CalculationError
import logging


def divide_numbers(a, b):
    try:
        if b == 0:
            raise CalculationError("Division by zero is not allowed")
        result = a / b
    except CalculationError as e:
        logging.error(f"Calculation error: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None
    else:
        return result
    finally:
        print("Execution of divide_numbers is complete.")


# Test the function
result = divide_numbers(10, 0)
if result is not None:
    print(f"Result: {result}")
