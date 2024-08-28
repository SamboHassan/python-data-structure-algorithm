def factorial(n):
    if n <= 1:
        # Base case
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)
