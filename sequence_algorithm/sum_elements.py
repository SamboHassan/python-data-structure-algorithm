def sum_element(S):
    """Return the sum of elements in sequence S"""
    n = len(S)
    sum = 0
    for e in range(n):
        sum += S[e]
    return sum


def sum_of_even_element(S):
    """Return sum of elements with even index"""

    total = 0
    for e in range(0, len(S), 2):
        total += S[e]
    return total


def sum_of_prefix_sum(S):
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total


def list_of_prefix(S):
    n = len(S)
    prefix = 0
    prefix_list = []
    for j in range(n):
        prefix += S[j]
        prefix_list.append(prefix)
    return prefix_list


from itertools import accumulate

seq = [1, 2, 3, 4, 5]
# print(sum_of_prefix_sum(seq))
# print(sum(accumulate(seq)))
# print()
# Prefix sum
a = [1, 2, 3, 4, 5]
b = [1, 3, 6, 10, 15]

# for n in accumulate(a):
#     print(n)

# print()
# print(list_of_prefix(a))
scores = {
    "Ahmed": 40,
    "Marya": 67,
    "Haladu": 30,
    "Jamelu": 90,
    "Bukar": 109,
    "Musa": 70,
}

high = {
    key: scores[key] for key in scores.keys() if scores[key] == max(scores.values())
}

print(high)
