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

Divide array into sub-arrays until each array contains a single element. Merge two arrays by iterating through them building a new merged array

### Advantages

 - Stable sort — equal elements preserve their original relative order.
 - Guaranteed O(n log n) in all cases; no worst-case degradation like Quick Sort.
 - Well-suited for linked lists (merge is cheap, no random access needed).
 - Naturally parallelisable — independent sub-arrays can be sorted concurrently.

### When Should I use it

 - When stability is required (e.g. sorting records that are already partially ordered by another field).
 - When guaranteed worst-case performance matters more than average-case speed.
 - When sorting linked lists or external data (e.g. data too large to fit in memory — merge sort maps well to disk-based sorting).

### Optimisation

 - **Bottom-up merge sort** — iterative version avoids recursion overhead and call-stack depth.
 - **Timsort** — Python's built-in `sorted()` uses Timsort, which detects natural runs in the input and uses insertion sort on small sub-arrays (threshold ~32–64 elements) before merging. This makes it very fast on real-world nearly-sorted data.
 - **In-place merging** — avoids the O(n) auxiliary space cost, but the merge step becomes significantly more complex.

### Complexity

| Case | Time | Space |
|---|---|---|
| Best | O(n log n) | O(n) |
| Average | O(n log n) | O(n) |
| Worst | O(n log n) | O(n) |

Unlike Quick Sort, Merge Sort always splits evenly, so all three cases are identical. The O(n) space cost comes from the temporary arrays used during the merge step.

### Code Snippets

```python
def merge_sort(arr: list) -> list:
    """
    Recursively split the array in half, sort each half, then merge.
    Returns a new sorted list — does not sort in-place.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    """
    Merge two sorted lists into one sorted list.
    Walk both lists with two pointers, always picking the smaller element.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= preserves stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements (at most one side will have leftovers)
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```



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


