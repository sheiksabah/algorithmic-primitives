# Searching Algorithms

This directory contains searching algorithms implemented from scratch in Python.

## Algorithms

### Binary Search

Binary search efficiently searches for a target value in a **sorted list** by repeatedly dividing the search space in half.

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`
- **Requirement:** Input must be sorted

### Hash Search

Hash search uses a hash function to map a key to an index in a hash table, allowing efficient lookup. This implementation uses separate chaining to handle collisions by storing multiple items in a bucket.

- **Average Time Complexity:** `O(1)` for lookup, assuming a good hash distribution and a bounded load factor
- **Worst-Case Time Complexity:** `O(n)` when many items collide
- **Collision Handling:** Separate chaining using lists

## Future Algorithms

- Linear Search
- Other searching algorithms as I learn them
