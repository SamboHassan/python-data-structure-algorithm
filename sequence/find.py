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
