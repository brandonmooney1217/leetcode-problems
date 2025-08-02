# LeetCode Problem Tracker

A Python-based project for organizing and tracking LeetCode problems by category with templates and utilities for efficient problem-solving practice.

## Project Structure

```
leetcode/
├── problems/                     # Problem solutions organized by category
│   ├── arrays/                   # Array problems
│   │   └── 001_two_sum/         # Example: Two Sum problem
│   │       ├── solution.py      # Solution implementation
│   │       └── README.md        # Problem documentation
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
├── tests/                        # Test files (mirrors problems structure)
│   └── arrays/
│       └── 001_two_sum/
│           └── test_solution.py  # Unit tests
├── templates/                    # Problem and test templates
├── scripts/                      # Utility scripts
│   ├── new_leetcode_problem.py  # Create new problem templates
│   ├── new_problem.py           # Interactive problem creator
│   └── generate_stats.py        # Progress statistics
└── CLAUDE.md                     # Development guide for Claude Code
```

## Getting Started

### Prerequisites
- Python 3.7+
- pip3

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
python3 scripts/new_leetcode_problem.py
```

This will prompt you for:
- Problem name
- Problem category

### Problem Structure
Each problem follows this structure:
```
problems/category/001_problem_name/
├── solution.py          # Main solution implementation
└── README.md           # Problem description and notes

tests/category/001_problem_name/
└── test_solution.py     # Unit tests
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

Run tests for a specific problem:
```bash
python3 -m pytest tests/arrays/001_two_sum/ -v
```

### Generating Statistics
View your solving progress:
```bash
python3 scripts/generate_stats.py
```

## Development Workflow

1. **Create new problem template:**
   ```bash
   python3 scripts/new_leetcode_problem.py
   ```

2. **Fill in problem details:**
   - Edit `README.md` with problem description, constraints, examples
   - Update `solution.py` with proper function signature

3. **Implement solution:**
   - Write your algorithm in the `solve()` method
   - Add time/space complexity analysis
   - Document your approach

4. **Write tests:**
   - Add test cases in `test_solution.py`
   - Include edge cases and performance tests

5. **Run tests:**
   ```bash
   python3 -m pytest tests/category/problem_name/ -v
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

## Example: Two Sum Problem

This repository includes a complete implementation of the Two Sum problem as an example:

- **Location**: `problems/arrays/001_two_sum/`
- **Algorithm**: Hash map approach with O(n) time complexity
- **Tests**: Comprehensive test suite with multiple cases

## Project Features

- **Organized Structure**: Problems categorized by algorithm type
- **Automated Setup**: Scripts to generate new problem templates
- **Testing Framework**: Comprehensive test structure with pytest
- **Progress Tracking**: Statistics generator to monitor solving progress
- **Documentation**: Standardized README templates for each problem
- **Development Guide**: CLAUDE.md for development with Claude Code

## Contributing

1. Follow the existing code structure
2. Include comprehensive test cases
3. Add clear problem descriptions and approach documentation
4. Update documentation as needed

## Template Usage

The templates provide a standardized structure for:
- Problem description and constraints
- Solution implementation with time/space complexity
- Comprehensive test cases
- Alternative approaches and optimizations

Happy coding! 🚀