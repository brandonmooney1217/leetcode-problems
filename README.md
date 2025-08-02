# LeetCode Problem Tracker

A Python-based project for organizing and tracking LeetCode problems by category with templates and utilities for efficient problem-solving practice.

## Project Structure

```
leetcode/
├── problems/                     # Problem solutions organized by category
│   ├── arrays/                   # Array problems
│   ├── strings/                  # String manipulation problems
│   ├── linked_lists/             # Linked list problems
│   ├── trees/                    # Binary trees and BST problems
│   ├── graphs/                   # Graph problems (BFS, DFS, etc.)
│   ├── dynamic_programming/      # Dynamic programming problems
│   ├── backtracking/             # Backtracking problems
│   ├── sorting_searching/        # Sorting and searching algorithms
│   ├── stack_queue/              # Stack and queue problems
│   ├── hash_tables/              # Hash table problems
│   ├── two_pointers/             # Two pointer technique
│   ├── sliding_window/           # Sliding window problems
│   └── math/                     # Mathematical problems
├── templates/                    # Problem and test templates
├── scripts/                      # Utility scripts
└── tests/                        # Test files
```

## Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone this repository
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

## Usage

### Creating a New Problem
Use the utility script to generate a new problem structure:

```bash
python3 scripts/new_problem.py
```

This will prompt you for:
- Problem category
- Problem number
- Problem name
- Difficulty level

### Problem Structure
Each problem follows this structure:
```
problems/category/001_problem_name/
├── solution.py          # Main solution implementation
├── test_solution.py     # Unit tests
└── README.md           # Problem description and notes
```

### Running Tests
Run all tests:
```bash
python3 -m pytest tests/
```

Run tests for a specific category:
```bash
python3 -m pytest tests/arrays/
```

### Generating Statistics
View your solving progress:
```bash
python3 scripts/generate_stats.py
```

## Problem Categories

- **Arrays**: Array manipulation, searching, sorting
- **Strings**: String processing, pattern matching
- **Linked Lists**: Singly/doubly linked list operations
- **Trees**: Binary trees, BST, tree traversal
- **Graphs**: BFS, DFS, shortest path, topological sort
- **Dynamic Programming**: Memoization, tabulation
- **Backtracking**: Recursive exploration with pruning
- **Sorting & Searching**: Various algorithms and optimizations
- **Stack & Queue**: LIFO/FIFO data structure problems
- **Hash Tables**: Hash maps, sets, frequency counting
- **Two Pointers**: Efficient array/string processing
- **Sliding Window**: Subarray/substring problems
- **Math**: Number theory, bit manipulation

## Contributing

1. Follow the existing code structure
2. Include comprehensive test cases
3. Add clear problem descriptions
4. Update documentation as needed

## Template Usage

The templates provide a standardized structure for:
- Problem description and constraints
- Solution implementation with time/space complexity
- Comprehensive test cases
- Alternative approaches and optimizations

Happy coding! 🚀