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

print(index)

print(list_data[index])
