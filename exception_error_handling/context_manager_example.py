"""
3. Using Context Managers for Resource Management
Context managers are a way to ensure that resources are 
properly managed, even in the presence of errors. The with 
statement is typically used to wrap the execution of a 
block of code that needs some "cleanup" after execution, 
like closing a file.

"""

import logging


class ManagedResource:
    def __enter__(self):
        print("Resource is being acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            logging.error(f"An error occurred: {exc_value}")
        print("Resource is being released")
        return True  # Prevents propagation of the exception


def use_resource():
    with ManagedResource() as resource:
        print("Using the resource")
        # Simulate an error
        raise InputError("An error occurred while using the resource")


# Test the context manager
use_resource()
