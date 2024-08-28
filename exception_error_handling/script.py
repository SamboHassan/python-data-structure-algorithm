import logging


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logging.error("Cannot divide by zero.")
        return None
    except NameError as e:
        logging.error(f"NameError: {e}")
        return None
    return result


# Usage:
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = divide(num1, num2)
    if result is not None:
        print(f"Result: {result}")
except NameError as e:
    print(f"NameError: {e}")
