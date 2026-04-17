# Dynamic Programming

## Description

A method of problem solving where a problem is broken down into smaller overlapping subproblems and the results of each sub-problem are stored (cached) to avoid redundant calculations. Dynamic programming uses memoization or tabulation to optimize recursive algorithms by trading space for time.

The classic example is fibonacci numbers, where each result is stored so that we do not need to re-calculate every time.

## When to Use Dynamic Programming

Dynamic Programming is ideal when your problem has these characteristics:

### 1. **Overlapping Subproblems**
The problem can be broken down into subproblems which are reused several times. For example, in Fibonacci:
- `fib(5)` calls `fib(4)` and `fib(3)`
- `fib(4)` calls `fib(3)` and `fib(2)`
- Notice `fib(3)` is calculated twice (overlapping)

### 2. **Optimal Substructure**
An optimal solution can be constructed from optimal solutions of its subproblems. The overall problem's best solution depends on solutions to smaller versions of the same problem.

### 3. **Avoid Re-computation**
Without memoization, recursive solutions recalculate the same subproblems exponentially (e.g., naive Fibonacci is O(2^n)). DP reduces this to polynomial time (e.g., O(n)).

### When NOT to Use DP:
- Problems without overlapping subproblems (pure divide-and-conquer)
- When space constraints are critical and you can't afford caching
- Simple problems where brute force is fast enough
- Problems that don't have optimal substructure

## What is Memoization?

### Definition
**Memoization** is a technique of caching (storing) the results of expensive function calls and returning the cached result when the same inputs occur again. It's a top-down approach to dynamic programming.

### How It Works
1. **Before computing**: Check if result already exists in cache
2. **Cache hit**: Return cached result immediately
3. **Cache miss**: Compute result, store in cache, return it
4. **Future calls**: Reuse cached result for same input

### Simple Example - Without Memoization (Inefficient):
```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1)
│   │   │   └── fib(0)
│   │   └── fib(1)        ← Recalculated!
│   └── fib(2)            ← Recalculated!
│       ├── fib(1)        ← Recalculated!
│       └── fib(0)
└── fib(3)                ← Entire subtree recalculated!
    ├── fib(2)            ← Recalculated!
    └── fib(1)            ← Recalculated!

Total calls: 15 (many duplicates)
```

### With Memoization (Efficient):
```
fib(5)
├── fib(4)
│   ├── fib(3) ✓ Cached
│   │   ├── fib(2) ✓ Cached
│   │   │   ├── fib(1) ✓ Cached
│   │   │   └── fib(0) ✓ Cached
│   │   └── fib(1) ✓ Return from cache (no recalculation)
│   └── fib(2) ✓ Return from cache
└── fib(3) ✓ Return from cache

Total calls: 6 (no duplicates, exponentially faster)
```

### Key Benefits:
- **Speed**: O(2^n) → O(n) for Fibonacci
- **Simplicity**: Minimal code changes needed
- **Automatic**: Decorators like `@functools.lru_cache` handle it automatically

### Trade-offs:
- **Memory**: Stores results for all computed inputs
- **Overhead**: Each lookup/storage has a small cost
- **Complexity**: Code is slightly more complex than pure recursion

## Fibonacci Numbers

### Full Implementation

```python
# The results dict must be global so that it is maintained across multiple calls to fibonacci_full_implementation.
results_dict = {}

def fibonacci_full_implementation(n: int) -> int:
    """
    Calculate the nth Fibonacci number using memoization (dynamic programming).
    
    Args:
        n: The position in the Fibonacci sequence
    
    Returns:
        The nth Fibonacci number
    """
    # First check if we have already calculated this result
    if n in results_dict:
        return results_dict[n]

    # The first two values in fibonacci sequence are 1.
    if n <= 1:
        result = n

    # Otherwise calculate the value
    else:
        result = fibonacci_full_implementation(n - 2) + fibonacci_full_implementation(n - 1)

    # Remember to add the result to the results dict. This is very important.
    results_dict[n] = result

    return result
```

### Production Implementation

In production code, leverage the `@functools.lru_cache` decorator for cleaner code.

```python
import functools

@functools.lru_cache(maxsize=None)
def fibonacci_production_implementation(n: int) -> int:
    """
    Calculate the nth Fibonacci number using memoization (dynamic programming).
    
    Args:
        n: The position in the Fibonacci sequence (non-negative integer)
    
    Returns:
        The nth Fibonacci number
    """
    # Base cases: fib(0) = 0, fib(1) = 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n-2) + fib(n-1)
    return fibonacci_production_implementation(n - 2) + fibonacci_production_implementation(n - 1)

```