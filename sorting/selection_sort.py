# ---------------- SELECTION SORT - another brute force/decrease and conquer

# It can be performed using an auxiliary array to store the results or
# done in place, meaning the original array is modified and no additional
# storage is required.


# The basic idea of selection sort is you find the smallest
# element in the array and you exchange it with the element in the first position.
# Then you repeat this process for the remaining items


def selection_sort(xs):
    for i in range(len(xs) - 1):
        min_index = i
        for j in range(i + 1, len(xs)):
            if xs[j] < xs[min_index]:
                min_index = j
        xs[i], xs[min_index] = xs[min_index], xs[i]


# So you next find the second smallest element in the array and you exchange
# it with the element in the second position. And you keep on doing this until
# the array is sorted.


def selection_sort(xs):
    for i in range(
        len(xs) - 1
    ):  # The last value will automatically be in correct position.
        # Find minimum value in unsorted region.
        min_index = i
        for j in range(i + 1, len(xs)):
            # Update min_index if the value at j is lower than current
            # minimum value.
            if xs[j] < xs[min_index]:
                min_index = j
        # After finding the minimum value in the unsorted region,
        # swap with the first unsorted value.
        xs[i], xs[min_index] = xs[min_index], xs[i]


# xs = [3, 2, 1, 5, 4]
xs = [-4, 2, 5, 8, -7, 3, 6, -1, 7]
print(xs)
selection_sort(xs)
print(xs)
print(
    all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1))
)  # A nice Pythonic way to check list is sorted.
