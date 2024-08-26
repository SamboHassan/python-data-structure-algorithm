print(ValueError.__mro__)
print(TypeError.__mro__)

# built-in exception typesbuilt-in exception types

""" 
Built-in Python Exceptions
Here is the list of default Python exceptions with descriptions:

AssertionError: raised when the assert statement fails.
EOFError: raised when the input() function meets the end-of-file condition.
AttributeError: raised when the attribute assignment or reference fails.
TabError: raised when the indentations consist of inconsistent tabs or spaces. 
ImportError: raised when importing the module fails. 
IndexError: occurs when the index of a sequence is out of range
KeyboardInterrupt: raised when the user inputs interrupt keys (Ctrl + C or Delete).
RuntimeError: occurs when an error does not fall into any category. 
NameError: raised when a variable is not found in the local or global scope. 
MemoryError: raised when programs run out of memory. 

ValueError: occurs when the operation or function receives an argument with the right type but the wrong value. 

ZeroDivisionError: raised when you divide a value or variable with zero. 
SyntaxError: raised by the parser when the Python syntax is wrong. 
IndentationError: occurs when there is a wrong indentation.
SystemError: raised when the interpreter detects an internal error.

"""


def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    elif x < 0:
        raise ValueError("x cannot be negative")
    else:
        return x**2


# Raise TypeError if argument is not a string
def validate_string(input):
    if not isinstance(input, str):
        raise TypeError("Input must be a string")


validate_string(42)  # Raises TypeError


# ValueError#
# A ValueError occurs when a function receives an argument of the
# expected type but an inappropriate value. Handle ValueError
# by validating arguments and inputs before passing to functions:

import math


def calc_square_root(num):
    if num < 0:
        raise ValueError("Number must be non-negative")
    return math.sqrt(num)


try:
    print(calc_square_root(-10))
except ValueError as e:
    print(e)  # Prints 'Number must be non-negative'


# ------------------ TypeError
# A TypeError happens when an operation or function is applied to
# an incompatible type. Adding extra type checking helps avoid TypeErrors:


def concatenate_strings(str1, str2):
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both arguments must be strings")
    return str1 + str2


# The try block allows you to test a block of code for errors.
# The except block lets you handle the error. The else block
# lets you execute code if no errors are raised, and the
# finally block allows you to execute code, regardless of the
# result.

# --------------- ImportError
# An ImportError occurs when Python cannot import a module.
# Catching this exception allows gracefully handling missing dependencies:

try:
    import pandas as pd
except ImportError:
    print("pandas not installed. Cannot import data")


# ----------------- OSError
# An OSError happens when a system operation fails, like unable to
# open a file, reach a network resource, or find a path.
# The error message usually indicates the underlying reason:

try:
    f = open("data.txt")
except OSError as e:
    print(f"Could not open file: {e}")


# ----------------- IndexError

# An IndexError indicates trying to access an element in a
# sequence that is out-of-bounds. Check array sizes before accessing
# elements to avoid this exception:


def get_first_element(arr):
    if len(arr) == 0:
        raise IndexError("Array is empty")
    return arr[0]


# Below is an example illustrating some recommended practices
# for clear, user-friendly error messages:


def process_json(input):
    try:
        data = json.loads(input)
    except ValueError as e:
        # Provide specific details
        msg = f"Unable to parse input as JSON. {e}"
        # Suggest fixes
        msg += " Ensure input is valid JSON format."
        raise ValueError(msg)
    except OSError as e:
        # Note for developer without exposing system details
        log.error(f"OSError {e}")
        raise Exception("A system error occurred. Please try again later")

    return data


"""
Exception Chaining
The from_traceback() function extracts exception details into a chained 
exception to avoid losing context from original failures.

Decorators
Decorator functions like @retry can automatically re-execute functions 
that failed, simplifying some types of error handling.

Exception Groups#
External libraries help group related exceptions and enable handling them 
together. For example, httpx.RequestError groups all request-related exceptions.

These tools supplement Python’s built-in exception handling capabilities. 
Evaluate external libraries carefully to avoid overly complicating code.

"""


def validate_string(input):
    if not isinstance(input, str):
        raise TypeError("Input must be a string")
    return input


print(validate_string("valid input"))


# ------------------ Finally Block  ----------------- #
# A finally block executes after a try/except block completes
# but before leaving the scope. This is useful for cleanup like closing files.

f = open("data.txt")
try:
    data = f.read()
except OSError:
    print("Could not read file")
finally:
    f.close()  # Closes file if open failed or succeeded


# ------------------ else Block
# An else block after try/except runs only if no exceptions occurred.
# This avoids needing to track success with a boolean flag:

success = False

try:
    num = int(user_input)
    success = True
except ValueError:
    print("Invalid number")
else:
    print(f"Input is {num}")
