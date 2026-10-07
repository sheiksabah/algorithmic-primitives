# Tests

This directory contains tests for the algorithms and machine learning implementations in this repository.

The tests are used to verify that each implementation produces the expected results across different inputs and edge cases.

## Testing Framework

Tests are written in Python using:

- **pytest**

## Test Structure

Each implementation should have a corresponding test file.

For example:

```text
searching/
└── binary_search.py

tests/
└── test_binary_search.py
```

## Running Tests

From the root directory of the repository, run:

```bash
pytest
```

To run a specific test file:

```bash
pytest tests/test_binary_search.py
```

## Testing Goals

Tests are designed to check:

- Expected outputs
- Edge cases
- Invalid or unusual inputs
- Boundary conditions
- Algorithm correctness
