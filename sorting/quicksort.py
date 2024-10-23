"""
Algorithm Overview

Quicksort is an efficient, comparison-based, divide-and-conquer sorting algorithm. 
It picks an element as a pivot and partitions the array into two halves, such that 
one half has elements less than the pivot and the other half has elements greater 
than the pivot. The process is recursively applied to the two halves until the 
entire array is sorted

Pseudocode 

Quicksort(arr, low, high):
    if low < high:
        pivot_index = Partition(arr, low, high)
        Quicksort(arr, low, pivot_index - 1)    # Recursively sort the left part
        Quicksort(arr, pivot_index + 1, high)   # Recursively sort the right part

Partition(arr, low, high):
    pivot = arr[high]          # Select pivot as the last element
    i = low - 1                # Index for the smaller element
    for j = low to high - 1:
        if arr[j] <= pivot:
            i = i + 1
            Swap arr[i] with arr[j]   # Move smaller element to the left
    Swap arr[i + 1] with arr[high]    # Move pivot to the correct position
    return i + 1                      # Return the pivot index

"""


def quicksort(arr, low, high):
    if low < high:
        # Partition the array
        pivot_index = partition(arr, low, high)

        # Recursively apply the same logic to the left and right subarrays
        quicksort(arr, low, pivot_index - 1)  # Sort the left part
        quicksort(arr, pivot_index + 1, high)  # Sort the right part


def partition(arr, low, high):
    pivot = arr[high]  # Taking the last element as pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements if condition met

    # Swap the pivot element to its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1  # Return the pivot index


"""
Key Points:

The pivot selection can affect the performance. This implementation uses the 
last element as the pivot, but other strategies include picking the first element, 
a random element, or the median. 

The average time complexity of Quicksort is O(n log n), but in the 
worst case (when the pivot is always the smallest or largest element), 
it can degrade to O(n²).

"""

# Example usage
arr = [10, 80, 30, 90, 40, 50, 70]
print("Original array:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


# ------ Second Approach


def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the two partitions
        quickSort(dataset, first, pivotIdx - 1)
        quickSort(dataset, pivotIdx + 1, last)


def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotvalue = datavalues[first]
    # establish the upper and lower indexes
    lower = first + 1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        # advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        # if the two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            # exchange the two values
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper


# test the merge sort with data
items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]
print(items)
quickSort(items, 0, len(items) - 1)
print(items)
