# Bubble Sort

## Overview

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

## Implementation

The `bubblesort.py` file contains a basic implementation of the bubble sort algorithm in Python.

```python
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```
## Example usage:
```python
if __name__ == "__main__":
    # Sample list
    my_list = [64, 34, 25, 12, 22, 11, 90]

    # Call the bubble_sort function
    bubble_sort(my_list)

    # Display the sorted list
    print("Sorted array:", my_list)
transfer into html
```

