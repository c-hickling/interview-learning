# Sorting Algorithms

## Quick Sort

### Description

Recursive algorithm where an array is sorted into higher or lower than a pivot value to create two sub-lists. Repeat process with each sub-list then when each sub-list is one element long, combine them in order.

### Advantages

 - Space efficient if implemented in-place (without creating any new lists)
 - Parallelisable as sub-lists can be treated independently.


### When Should I use it

 - Large datasets as it can be made very space efficient and it is parallelisable

### Optimisation

 - Pick 3 values at random and then take the middle value.
 - Sublists can be processed independently so it can be very parallelisable

### Complexity

| Case | Time | Space (out-of-place) |
|---|---|---|
| Average | O(n log n) | O(n) |
| Worst | O(n²) | O(n) |

The worst case occurs when the pivot is always the minimum or maximum element (e.g. already-sorted input with a naïve first/last pivot). This degenerates into n recursive calls each of size n-1, giving O(n²). The median-of-three optimisation reduces the likelihood of hitting this case.

### Code Snippets

```python
def quick_sort(list_to_sort: list) -> list:
    """
    Recursively sort a list using the quick sort algorithm.
    Picks the middle element as pivot, partitions into values less than
    and greater than the pivot, then recurses on each partition. Recombine in order.
    """
    if len(list_to_sort) <= 1:
        return list_to_sort

    # Take the middle value in the unsorted list as the pivot point
    pivot_value = list_to_sort[len(list_to_sort) // 2]

    left_list = []
    right_list = []
    equal_list = []

    for item in list_to_sort:
        if item < pivot_value:
            left_list.append(item)
        elif item > pivot_value:
            right_list.append(item)
        else:
            equal_list.append(item)

    return quick_sort(left_list) + equal_list + quick_sort(right_list)
```

```python
def _median_of_three(arr: list, low: int, high: int) -> int:
    """
    Finds the median of arr[low], arr[mid], arr[high], places it at arr[high],
    and returns it. This gives a statistically better pivot than always picking
    first/last, reducing the chance of O(n²) worst-case behaviour.
    """
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    # arr[mid] is now the median — move it to high-1 so Lomuto
    # partitioning leaves the two boundary elements (arr[low] ≤ pivot ≤ arr[high])
    # out of the inner loop, saving two comparisons per call.
    arr[mid], arr[high] = arr[high], arr[mid]
    return arr[high]


def _partition(arr: list, low: int, high: int) -> int:
    """
    Lomuto partition: everything ≤ pivot ends up left of the returned index,
    everything > pivot ends up right of it.
    """
    pivot = _median_of_three(arr, low, high)
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Place pivot in its final sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_optimised(arr: list, low: int = 0, high: int = None) -> None:
    """
    In-place quicksort using median-of-three pivot selection.

    Sorts arr directly — no new lists are allocated (O(log n) stack space only).
    Call as quick_sort_optimised(my_list) for the full list.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = _partition(arr, low, high)
        quick_sort_optimised(arr, low, pivot_idx - 1)
        quick_sort_optimised(arr, pivot_idx + 1, high)
```

## Merge Sort

### Description


### Advantages



### When Should I use it



### Optimisation



### Complexity



### Code Snippets



## Bubble Sort

### Description


### Advantages



### When Should I use it



### Optimisation



### Complexity



### Code Snippets



## Insertion Sort

### Description


### Advantages



### When Should I use it



### Optimisation



### Complexity



### Code Snippets



## Selection Sort

### Description


### Advantages



### When Should I use it



### Optimisation



### Complexity



### Code Snippets


