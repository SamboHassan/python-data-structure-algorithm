def factorial_iterative2(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result
