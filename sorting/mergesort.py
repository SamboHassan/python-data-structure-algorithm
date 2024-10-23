"""
Pseudocode for Merge Sort
Merge Sort is a divide and conquer algorithm that works by splitting the array 
into two halves, recursively sorting both halves, and then merging the sorted 
halves together.

-----divide part
function mergeSort(array):
    if array has 1 or 0 elements:
        return array

    split array into two halves:
        left_half = array[0..mid]
        right_half = array[mid+1..n]

    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    return merge(left_half, right_half)



------conquer part
function merge(left, right):
    create an empty result array
    while both left and right are not empty:
        if left[0] <= right[0]:
            append left[0] to result
            remove left[0] from left
        else:
            append right[0] to result
            remove right[0] from right
    
    append remaining elements of left (if any) to result
    append remaining elements of right (if any) to result
    
    return result


Explanation of the Pseudocode:

1. Base case: If the array has one or zero elements, it's already sorted.
2. Divide: Split the array into two halves.
3. Conquer: Recursively apply merge sort to both halves.
4. Merge: Combine the two sorted halves into one sorted array by comparing elements 
   and building the result.


Example Execution:
For the array [38, 27, 43, 3, 9, 82, 10]:

1. The array is split into two halves [38, 27, 43] and [3, 9, 82, 10].
2. Each half is recursively split until we have arrays of size 1.
3. The sorted arrays are then merged step by step, resulting in the final sorted array.
4. The sorted array becomes: [3, 9, 10, 27, 38, 43, 82].

"""


def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point
        mid = len(arr) // 2

        # Divide the array elements into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves
        i = j = k = 0

        # Copy data to temporary arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array is:", arr)


# -----------------  Merge sort2


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # recursively break down the arrays
        mergeSort(leftarr)
        mergeSort(rightarr)

        # now perform the merging
        i = 0  # index into the left array
        j = 0  # index into the right array
        k = 0  # index into merged array

        # while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

# test the merge sort with data
print(items)
mergesort(items)
print(items)


"""

Results-driven Engineer, dedicated to building elite teams that consistently 
achieve business objectives and drive profitability. With over 8 years of 
experience, spannning different facets of the FinTech space; including digital 
lending, consumer payment, collections and payment gateway using Java/Spring Boot 
technologies, PHP and Ruby on Rails

"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
