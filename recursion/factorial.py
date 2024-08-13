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


y = factorial_iterative(4)
print(y)
