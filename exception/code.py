def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    elif x < 0:
        raise ValueError("x cannot be negative")
    else:
        return x**x


# answer = square("9")
# print(answer)

# How much error-checking to perform within a function is a matter of debate.


# def sqr2(x):
#     if not isinstance(x, int, float):
#         raise TypeError("x must be numeric")

# FINDING THE LARGEST VALUE IN A LIST OF ELEMENTS
# Assuming that the list has at least one largest element


def find_largest_val(data):
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest


list_data = [32, 6, 53, 8, 90, 3, 5, 65]

# print(find_largest_val(data))


# INDEX BASED FOR LOOP
# Finding the index of the biggest element
def find_max_index(data):
    big_index = 0
    for j in range(len(data)):
        if data[j] > data[big_index]:
            big_index = j
    return big_index


index = find_max_index(list_data)

# print(index)

# print(list_data[index])


# def scale(data, factor):
#     for j in range(len(data)):
#         data[j] *= factor
#     return data


list2_data = [2, 3, 4, 1, 2]

# print(list2_data)
# print(scale(list2_data, 2))
# print(list2_data)
# print("a", "b", "c", sep=":")


def scale(data, factor):
    """_Multiply all entries of numeric data by the given factor_

    Args:
        data (iterable sequence): an instance of any sequence type (such as a list)
        containig numeric elements

        factor (int): a number that servers as the multiplicative factor for scaling

    Returns:
        list: a new list that contain the
    """

    for j in range(len(data)):
        data[j] *= factor
    return data


list = [2, 2, 2, 2]
data = {"one": 1, "two": 2, "three": 3, "four": 4}
# print(scale(list, 4))


# i = iter(data)

# print(i.next())


def factors(n):
    results = []
    for j in range(1, n + 1):
        if n % j == 0:
            results.append(j)
    return results


# print(factors(200))


def factor2(n):
    for j in range(1, n + 1):
        if n % j == 0:
            yield j


first = factor2(20)

print(first)

it_list = ["one", "two", "three"]
it = iter(it_list)

print(next(it))
print(next(it))
print(next(it))
