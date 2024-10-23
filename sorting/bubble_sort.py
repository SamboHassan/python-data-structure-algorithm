"""
Pseudocode for Bubble Sort
Bubble Sort works by repeatedly swapping adjacent elements if 
they are in the wrong order. This process "bubbles" the largest 
unsorted element to its correct position in each iteration. Here’s 
the pseudocode:Pseudocode for Bubble Sort Bubble Sort works by 
repeatedly swapping adjacent elements if they are in the wrong 
order. This process "bubbles" the largest unsorted element to 
its correct position in each iteration. 

Here’s the pseudocode:

for i from 0 to length_of_array - 1:
    for j from 0 to length_of_array - i - 1:
        if array[j] > array[j + 1]:
            swap(array[j], array[j + 1])


Explanation of the Pseudocode:

The outer loop runs n-1 times (where n is the length of the array) to ensure the 
array is sorted. The inner loop compares adjacent elements and swaps them if they 
are out of order. After each pass, the largest unsorted element moves to the correct 
position, reducing the number of comparisons needed in subsequent passes.

Example Execution:
For the array [64, 34, 25, 12, 22, 11, 90]:

1. After the first pass, 90 moves to the end.
2. After the second pass, 64 moves just before 90.
3. The process continues, and after several passes, the array becomes fully 
   sorted


Optimized Version:
The swapped flag ensures that if no elements are swapped during a pass, the array 
is already sorted, and the algorithm can terminate early.

Time Complexity:
Best case: O(n) (when the array is already sorted, and no swaps are made).
Worst case: O(n^2) (when the array is sorted in reverse order).
Average case: O(n^2).

Space Complexity:
Space complexity: O(1) (in-place sorting algorithm).

"""


# Bubble sort algorithm


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


# Example usage
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(arr)
# print("Sorted array is:", arr)


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Track if a swap was made in the current pass
        swapped = False

        # Last i elements are already sorted, so skip them
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break


def bubbleSort(dataset):
    # start with the array length and decrement each time
    for i in range(len(dataset) - 1, 0, -1):
        # examine each item pair
        for j in range(i):
            # swap items if needed
            if dataset[j] > dataset[j + 1]:
                temp = dataset[j]
                dataset[j] = dataset[j + 1]
                dataset[j + 1] = temp

        print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Starting state: ", list1)
    bubbleSort(list1)
    print("Final state: ", list1)


if __name__ == "__main__":
    main()
