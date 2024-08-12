# develop a method computePrefixAvg that takes an array arr storing n integers,
# where n >= 1 and returns an array containing prefix averages of the
# array passed to computePrefixAvg. Function computePrefixAvg runs in linear time.


def prefix_average(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total // (j + 1)
    return A


list1 = [12, 14, 13, 15, 19, 17, 16, 11, 18, 20]
ans = [12, 13, 13, 13, 14, 15, 15, 14, 15, 15]

list2 = [6, 3, 5, 8]

x = prefix_average(list1)

print(x)

# def pav(S):
# 	n = len(S)
# 	A = [0] * n
