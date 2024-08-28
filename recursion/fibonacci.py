def good_fibonacci(n):
    """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)

    return (a + b, a)


def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]
