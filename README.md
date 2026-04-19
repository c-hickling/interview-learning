# Interview Learning Repository

A curated collection of essential algorithms, data structure techniques, and design patterns for technical interview preparation.

## Table of Contents

- [Overview](#overview)
- [Sorting Algorithms](#sorting-algorithms)
- [LeetCode Algorithms](#leetcode-algorithms)
- [Dynamic Programming](#dynamic-programming)
- [Design Patterns](#design-patterns)
- [Repository Structure](#repository-structure)

## Overview

This repository documents practical algorithms commonly encountered in technical interviews. Each algorithm includes:
- **Description**: How the algorithm works
- **When to use**: Ideal use cases and scenarios
- **Code snippets**: Python implementations
- **Complexity analysis**: Time and space complexity

## Sorting Algorithms

Documentation: [`sorting-algo.md`](sorting-algo.md)

Core sorting techniques covering advantages, optimizations, and complexity analysis:

1. **Quick Sort** - Divide and conquer with pivot selection
   - Best for large datasets with space efficiency concerns
   - Average O(n log n), worst-case O(n²)
   - Parallelizable and space-efficient

2. **Merge Sort** - Stable divide-and-conquer approach
   - Guaranteed O(n log n) across all cases
   - Excellent for linked lists and nearly-sorted data
   - Naturally parallelizable

3. **Bubble Sort** - Simple comparison-based sorting
   - O(n²) average and worst-case
   - Best for teaching; rarely used in practice
   - In-place with O(1) space

4. **Insertion Sort** - Incremental sorting approach
   - O(n²) for random data; O(n) for nearly-sorted
   - Used internally by Timsort for small sub-arrays
   - Excellent for small arrays and online sorting

5. **Selection Sort** - Minimum-finding approach
   - O(n²) in all cases
   - Minimizes write operations (useful for expensive writes)
   - Simple in-place algorithm

## LeetCode Algorithms

Documentation: [`basic-algo.md`](basic-algo.md)

Key problem-solving techniques and patterns:

1. **Binary Search** - Efficient searching on sorted data
   - O(log n) time complexity
   - Used for: locating values, insertion positions
   - Requires ordered datasets

2. **Two Pointers** - Optimal for paired matching problems
   - Reduces O(n²) brute-force to O(n)
   - Used for: sum targets, palindromes, partitioning
   - Works on sorted arrays and strings

3. **Sliding Window** - Contiguous element subproblems
   - O(n) time for variable-length windows
   - Used for: max/min sums, longest valid substrings
   - Expands and contracts over sequences

4. **Breadth First Search (BFS)** - Level-order graph traversal
   - O(V + E) time and space complexity
   - Best for: shortest path problems, level-order exploration
   - Uses a queue for iterative traversal

5. **Depth First Search (DFS)** - Exhaustive path exploration
   - O(V + E) time and space complexity
   - Best for: path existence, backtracking, puzzles
   - Uses recursion and stack

## Dynamic Programming

Documentation: [`dynamic-programming.md`](dynamic-programming.md)

Optimization technique for solving problems with overlapping subproblems and optimal substructure:

### When to Use:
- **Overlapping Subproblems** - Same calculations needed multiple times
- **Optimal Substructure** - Optimal solution built from optimal subproblems
- **Exponential to Polynomial** - Convert O(2^n) brute-force to O(n) or better

### Memoization Explained:
- **Definition**: Caching function results to avoid redundant calculations
- **Top-down approach**: Start with main problem, break into subproblems, cache results
- **Trade-off**: Space cost (memory) for speed gain (time)
- **Example**: Fibonacci without memoization = 15 calls; with memoization = 6 calls

### Implementations:
1. **Full Implementation** - Educational manual memoization with dictionary
   - Shows cache management mechanics
   - Global state for result storage
   - Best for: Learning and understanding the concept

2. **Production Implementation** - Pythonic decorator-based approach
   - Uses `@functools.lru_cache(maxsize=None)`
   - Automatic cache management
   - Clean, maintainable code
   - Best for: Real-world production code

Both implementations use Fibonacci as the example, achieving O(n) time complexity.

## Design Patterns

Documentation: [`Design Patterns/`](Design%20Patterns/)

Reusable solutions to common problems in software design, particularly useful for interviews to demonstrate architectural knowledge:

### Singleton Pattern
**Purpose**: Restrict a class to a single instance while providing global access to that instance.

**When to Use**: Database connections, configuration managers, loggers, thread pools, caching systems
**When NOT to Use**: Testing is critical, dependency injection is possible, or simplicity matters more

**Key Implementations**:
1. **Basic Singleton** - Simple `__new__` override (⚠️ NOT thread-safe)
2. **Thread-Safe Singleton** - Double-checked locking (✅ Production-grade)
3. **Decorator-Based** - Clean, Pythonic approach (✅ Recommended)
4. **Module-Level Singleton** - Simplest Python approach (✅ Most Pythonic)

**Trade-offs**: Controlled access vs testing difficulties; guaranteed instance vs hidden dependencies

### Factory Method Pattern
**Purpose**: Create objects without specifying exact classes, decoupling creation logic from client code.

**When to Use**: Multiple related types, runtime decisions, reducing dependencies, extensibility
**When NOT to Use**: Single class only, simple cases, or when overengineering

**Key Implementations**:
1. **Simple Factory** - Static method with conditionals (Simplest)
2. **Factory Method** - Inheritance-based (Most extensible)
3. **Registry-Based** - Dynamic registration of types (Flexible)
4. **Configuration-Driven** - Plugins loaded from config (External management)

**Trade-offs**: Loose coupling vs added complexity; extensibility vs indirection overhead

**Recommendation**: Use for multiple object types. Prefer Dependency Injection when possible.

### Strategy Pattern
**Purpose**: Define a family of algorithms, encapsulate each one, and make them interchangeable.

**When to Use**: Multiple similar algorithms, runtime selection, replacing if/elif chains
**When NOT to Use**: Single algorithm, simple conditionals, or when overengineering

**Key Implementations**:
1. **Simple Strategy** - Object-oriented with abstract base class (Clear, basic)
2. **Factory-Based** - Automated strategy selection (Clean separation)
3. **Registry-Based** - Dynamic registration of strategies (Flexible, extensible)
4. **Functional** - Lambda/function-based strategies (Pythonic, minimal code)

**Trade-offs**: Eliminates conditionals vs added complexity; flexibility vs indirection overhead

**Real-World Examples**: Payment processing, sorting algorithms, compression, authentication, data export

### Observer Pattern
**Purpose**: Define one-to-many dependency where state change in one object notifies all dependents automatically (Pub-Sub).

**When to Use**: Event systems, MVC/MVVM architectures, real-time updates, change notifications, UI reactivity
**When NOT to Use**: Tight coupling acceptable, few notifications needed, simple direct calls sufficient

**Key Implementations**:
1. **OOP-Based** - Abstract subject/observer classes (Explicit, structured)
2. **Event-Based** - Callback functions, EventEmitter (Simple, Pythonic)
3. **Decorator-Based** - @subscribe decorator syntax (Elegant, concise)
4. **Property-Based** - Observable properties (Fine-grained control)

**Trade-offs**: Loose coupling vs memory leak risks; scalability vs notification overhead; flexibility vs debugging difficulty

**Common Pitfalls**: Memory leaks, observer order dependencies, circular dependencies, modifying during notification, unnecessary notifications

**Real-World Examples**: GUI frameworks, stock market, game development, MVC/MVVM, React/Vue, Node.js EventEmitter

## Repository Structure

```
interview-learning/
├── README.md                    # This file
├── sorting-algo.md              # Detailed sorting algorithm guide
├── basic-algo.md                # Common interview problem patterns
├── dynamic-programming.md       # Dynamic programming with memoization
└── Design Patterns/             # Reusable design patterns
    ├── singleton.md             # Singleton pattern
    ├── factory.md               # Factory method pattern
    ├── strategy.md              # Strategy pattern
    └── observer.md              # Observer/Subject pattern
```

---

**Last Updated**: 2026-04-17
