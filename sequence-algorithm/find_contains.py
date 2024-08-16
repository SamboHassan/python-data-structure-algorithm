def find(S, val):
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j


def find(S, val):
    """Return index j such that S[j]== val, or -1 if no such element"""
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j
        j += 1
    return -1


S = [3, 4, 5, 7, 8, 23, 45, 6, 8]

print(find(S, 23))


def contains(data, target):
    for item in data:
        if item == target:  # found a match
            return True
    return False


print(contains(data, 9))


def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n


print(count(data, 4))
