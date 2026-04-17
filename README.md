# Interview Learning Repository

A curated collection of essential algorithms and data structure techniques for technical interview preparation.

## Table of Contents

- [Overview](#overview)
- [Sorting Algorithms](#sorting-algorithms)
- [LeetCode Algorithms](#leetcode-algorithms)
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

Documentation: [`leetcode-algo.md`](leetcode-algo.md)

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

## Repository Structure

```
interview-learning/
├── README.md              # This file
├── sorting-algo.md        # Detailed sorting algorithm guide
└── leetcode-algo.md       # Common interview problem patterns
```

---

**Last Updated**: 2026-04-17
