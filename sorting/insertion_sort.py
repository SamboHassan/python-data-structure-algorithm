# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):  # from 1 to n-1
        cur = A[k]  # current element to be inserted
        j = k  # find correct index j for current
        while j > 0 and A[j - 1] > cur:  # element A[j-1] must be after current
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur  # cur is now in the right place



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        

def insertionSort(lst):
    for i in range(1, len(lst)):
      # insert lst[i] into a sorted sublist lst[0..i-1] so that
      # lst[0..i] is sorted.
      currentElement = lst[i]
      k = i - 1
      while k >= 0 and lst[k] > currentElement:
        lst[k + 1] = lst[k]
        k -= 1
     # Insert the current element into lst[k+1]
     lst[k + 1] = currentElement




# Insertion sort works by building a sorted section of the array one 
# element at a time.

"""
PSEUDOCODE 

for i from 1 to length_of_array - 1:
    key = array[i]
    j = i - 1
    
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]  # Shift elements of the sorted segment
        j = j - 1
    
    array[j + 1] = key  # Insert the key into the correct position

Two pointers 
i = 1
j = i-1 = 0 --j is always 1 less than j

"""

"""
Explanation of the Pseudocode:

1. Start from the second element (index 1) because the first element is considered 
   sorted.
2. Select the current element as the key.
3. Compare the key with elements in the sorted part (left side) of the array.
4. Shift elements greater than key to the right, creating a space for key.
5. Insert the key at its correct position in the sorted part of the array.
6. Repeat the process until the array is sorted.

Time Complexity:
1. Best case: O(n) (when the array is already sorted).
2. Worst case: O(n^2) (when the array is sorted in reverse order).
3. Average case: O(n^2).
Space Complexity:
- Space complexity: O(1) (in-place sorting algorithm).

"""

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Select the element to be inserted
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one 
        # position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift the larger element to the right
            j -= 1
        
        # Place the key at the correct position
        arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array is:", arr)
