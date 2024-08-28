# Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial_iterative(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1

    i = 0
    f = 1
    while i < num:
        i = i + 1
        f = f * i

    return f


def factorial_recursive(n):
    if type(n) is not int:
        return None
    if n < 0:
        return None
    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)


x = factorial_iterative(4)
y = factorial_recursive(4)
print(x)
print(y)
