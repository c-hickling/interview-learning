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

Repeatedly step through the array, comparing adjacent pairs and swapping them if they are in the wrong order. Each full pass bubbles the largest unsorted element to its correct position at the end. Repeat until no swaps occur.

### Advantages

 - Simple to implement and understand.
 - Stable sort — equal elements are never swapped, so relative order is preserved.
 - Detects an already-sorted array in O(n) with the early-exit optimisation.

### When Should I use it

 - Rarely in practice — mainly for teaching purposes.
 - When the input is known to be nearly sorted and you need a simple in-place stable sort.

### Optimisation

 - **Early exit** — track whether any swap occurred during a pass. If none did, the array is already sorted and you can stop early (best case becomes O(n)).
 - **Shrinking upper bound** — after each pass, the last `i` elements are guaranteed sorted, so shorten the inner loop by one each time.

### Complexity

| Case | Time | Space |
|---|---|---|
| Best (already sorted) | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) | O(1) |

The O(1) space is because sorting is done in-place with only a temporary swap variable.

### Code Snippets

```python
def bubble_sort(arr: list) -> None:
    """
    Sort arr in-place using bubble sort.
    Each pass bubbles the largest unsorted element to its final position.
    Exits early if a pass completes with no swaps (array is already sorted).
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        # Inner loop shrinks each pass — last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # No swaps means the array is sorted — exit early
```



## Insertion Sort

### Description

Build a sorted sub-array one element at a time. For each new element, shift all larger elements in the sorted portion one position to the right, then insert the new element into the gap left behind.

### Advantages

 - Simple to implement.
 - Stable sort — equal elements are never moved past each other.
 - In-place — O(1) extra space.
 - Very efficient on small or nearly-sorted arrays; used internally by Timsort for small sub-arrays.
 - Online algorithm — can sort a list as it receives elements one at a time.

### When Should I use it

 - Small arrays (typically n < 20) where overhead of recursive algorithms is not worth it.
 - Nearly-sorted data — each element only needs to move a short distance.
 - As the base case in hybrid sorts like Timsort or Introsort.

### Optimisation

 - **Binary search insertion** — use binary search to find the correct insertion position in O(log n) comparisons, though shifting still costs O(n) so overall time stays O(n²).
 - **Shell sort** — generalisation of insertion sort that allows swapping elements far apart first, reducing the total amount of shifting needed.

### Complexity

| Case | Time | Space |
|---|---|---|
| Best (already sorted) | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) | O(1) |

Best case is O(n) because each element only needs one comparison to confirm it is already in the right position — no shifts required.

### Code Snippets

```python
def insertion_sort(arr: list) -> None:
    """
    Sort arr in-place using insertion sort.
    Maintains a sorted left portion, inserting each new element into its
    correct position by shifting larger elements one step to the right.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements of the sorted portion that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert key into the gap left by shifting
        arr[j + 1] = key
```



## Selection Sort

### Description


### Advantages



### When Should I use it



### Optimisation



### Complexity



### Code Snippets


