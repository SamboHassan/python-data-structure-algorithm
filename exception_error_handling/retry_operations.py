"""
Advanced Example: Handling Multiple Exceptions and Retrying 
Operations Sometimes, you need to retry an operation if it 
fails, especially when dealing with unreliable resources 
like network requests.

"""
import time
import random
from custom_exceptions import CalculationError
import logging


def unreliable_operation():
    # Simulate an operation that might fail
    if random.choice([True, False]):
        raise CalculationError("Random failure occurred")
    return "Success"


def perform_operation_with_retries(retries=3):
    attempt = 0
    while attempt < retries:
        try:
            result = unreliable_operation()
            return result
        except CalculationError as e:
            logging.error(f"Attempt {attempt + 1} failed: {e}")
            attempt += 1
            time.sleep(2)  # Wait before retrying
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            break
    return None


# Test the function with retries
result = perform_operation_with_retries()
if result:
    print(f"Operation succeeded: {result}")
else:
    print("Operation failed after multiple attempts")
