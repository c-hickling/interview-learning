# LeetCode Algorithms

## Binary Search

### Description

Decrease and conquer algorithm where by the size of the problem space is halved each time. Requires an ordered dataset. Split the data in two around a central pivot point. If the outcome is less than the pivot point take the left hand side, if it is more than the pivot point take the right hand side. If it is equal to the pivot point that is the result. Repeat until the correct value is found. 

### When should I use it

We have an ordered set of data and want to find where a particular value sits. For example, where in an ordered list should I insert value X to maintain order.

### Code Snippet

``` python
def binary_search(ordered_list: list[int], match_value: int, left_hand_bound: int = None, right_hand_bound: int = None) -> int:
    """
    Basic binary search algorithm.
    """

    if left_hand_bound is None:
        left_hand_bound = 0

    if right_hand_bound is None:
        right_hand_bound = len(ordered_list) - 1


    # Find the pivot value by taking the centre point.
    pivot_point = left_hand_bound + (right_hand_bound - left_hand_bound) // 2



    if match_value > ordered_list[pivot_point]:
        return binary_search(ordered_list, match_value, left_hand_bound = pivot_point, right_hand_bound = right_hand_bound)
    elif (match_value < ordered_list[pivot_point]):
        return binary_search(ordered_list, match_value, left_hand_bound = left_hand_bound, right_hand_bound = pivot_point)
    else:
        return ordered_list[pivot_point]
```

### Complexity

O(log n) time complexity.

O (1) space complexity if we do not create any new lists and just shift the window we are looking in.


## Two Pointers

### Description

Two pointers maintains two indices into a sequence that move toward (or away from) each other, or in the same direction at different speeds. This avoids a nested loop and reduces an O(n²) brute-force scan down to O(n).

### When should I use it

Use it on sorted arrays or strings when you need to find a pair (or triplet) satisfying a condition — e.g. two numbers that sum to a target, or checking whether a string is a palindrome. Also used for in-place operations like removing duplicates or partitioning an array.

### Code Snippet

``` python
def two_sum_sorted(numbers: list[int], target: int) -> tuple[int, int]:
    """
    Find two indices whose values sum to target in a sorted list.
    Uses opposite-end pointers: if the sum is too large shrink from
    the right; if too small grow from the left.

    Args:
        numbers: Sorted list of integers
        target: The desired sum

    Returns:
        Tuple of the two indices (1-indexed), or (-1, -1) if not found
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return (left + 1, right + 1)
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return (-1, -1)
```

### Complexity

O(n) time complexity — each pointer moves at most n steps in total.

O(1) space complexity — no extra data structures needed.

## Sliding Window

### Description

A subset of the two pointers algorithm where a left and right pointer define a window over a sequence. The window expands by advancing the right pointer and shrinks by advancing the left pointer, avoiding the need to reprocess elements. The window can be fixed length or variable length.

### When should I use it

Any problem that asks for contiguous elements in a string or an array. For example, max/min sum of a contiguous subarray of size k (fixed window) or longest subarray satisfying a constraint (variable window).

### Code Snippet

``` python
def longest_unique_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    Uses a variable-size sliding window — expand rhs until a duplicate is
    found, then shrink from lhs until the window is valid again.

    Args:
        s: Input string

    Returns:
        Length of the longest substring with all unique characters
    """
    seen = set()
    lhs = 0
    best = 0

    for rhs in range(len(s)):
        # Shrink from the left until the duplicate is evicted
        while s[rhs] in seen:
            seen.remove(s[lhs])
            lhs += 1

        seen.add(s[rhs])
        best = max(best, rhs - lhs + 1)

    return best
```

### Complexity

O(n) time complexity — each character is added and removed from the set at most once.

O(k) space complexity where k is the size of the character set (bounded by 26 for lowercase alpha).

## Breadth First Search (BFS)

### Description

BFS is an iterative algorithm uses queue to move through a tree structure ensuring that every node on a given level is seen before moving on to the next level. 

### When should I use it

Finding the shortest possible route when many are available, such as in mapping.

### Code Snippet

``` python
from collections import deque

def bfs(graph: dict, start_node: str) -> list:
    """
    Generic BFS algorithm for traversing a graph.
    
    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}
        start_node: The node to start traversal from
    
    Returns:
        List of nodes in BFS order
    """
    visited = set()
    queue = deque([start_node])
    result = []
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add unvisited neighbors to queue
            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
    
    return result
```

### Complexity

O(V + E) time complexity where V is vertices and E is edges.

O(V) space complexity for the visited set and queue.

## Depth First Search (DFS)

### Description

A recursive backtracking algorithm that leverages the stack to move through a tree structure.

### When should I use it

It should be used to determine if a path exists between two nodes or to perform an exhaustive search of a tree. It should also be used for solving puzzles (such as mazes or the N-Queens problem) when you need to be able to go deep down a particular path and then backtrack when you get to a point of failure.  

### Code Snippet

``` python
def dfs(graph: dict, start_node: str) -> list:
    """
    Generic DFS algorithm for traversing a graph.
    
    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}
        start_node: The node to start traversal from
    
    Returns:
        List of nodes in DFS order
    """
    visited = set()
    result = []

    def perform_search(node: str) -> None:
        visited.add(node)
        result.append(node)

        # Recurse into each unvisited neighbour
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    perform_search(neighbor)

    perform_search(start_node)
    return result
```

### Complexity

O(V + E) time complexity where V is vertices and E is edges.

O(V) space complexity for the visited set and the implicit call stack (bounded by max depth).
