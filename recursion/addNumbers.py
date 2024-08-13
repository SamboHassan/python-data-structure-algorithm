# This prints the sum of all of the numbers from 1 to n


def addNumbers_iterative(i):
    counter = 0
    sum = 0
    while counter < i:
        counter += 1
        sum += counter
    return sum


def addNumbers_recursive(i):
    if i == 0:
        return 0
    return i + addNumbers(i - 1)


print(addNumbers(10))
print(addNumbers_iterative(10))
