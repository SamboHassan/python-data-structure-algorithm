def sum_element_prefix(A, B):
    """Assume that A and B have equal length.

    Return the number of (counts) elements in B equal to the sum of prefix sums in A
    """
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1 + j):
                total += A[k]
        if B[i] == total:
            count += 1
    return count
