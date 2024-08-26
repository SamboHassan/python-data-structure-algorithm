# traditional function that computes factors
def factors(n):
    results = []  # store factors in a new list
    for k in range(1, n + 1):
        if n % k == 0:  # divides evenly, thus k is a factor
            results.append(k)  # add k to the list of factors
    return results  # return the entire list


# generator that computes factors
def factors(n):
    for k in range(1, n + 1):
        if n % k == 0:  # divides evenly, thus k is a factor
            yield k  # yield this factor as next result


# generator that computes factors
def factors(n):
    k = 1
    while k * k < n:  # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:  # special case if n is perfect square
        yield k
