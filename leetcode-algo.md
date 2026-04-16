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

### When should I use it

### Code Snippet

``` python

```

### Complexity

## Sliding Window

### Description

### When should I use it

### Code Snippet

``` python

```

### Complexity

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

## Depth First Search

### Description

### When should I use it

### Code Snippet

``` python

```

### Complexity

