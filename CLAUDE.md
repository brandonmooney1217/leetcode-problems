# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Development Setup
```bash
pip3 install -r requirements.txt
```

### Testing
```bash
# Run all tests
python3 -m pytest tests/

# Run tests for specific category
python3 -m pytest tests/arrays/

# Run tests with coverage
python3 -m pytest tests/ --cov

# Run single test file
python3 -m pytest tests/arrays/001_problem_name/test_solution.py
```

### Code Quality
```bash
# Format code
black .

# Sort imports
isort .

# Lint code
flake8 .

# Type checking
mypy .
```

### Project Utilities
```bash
# Create new problem (interactive)
python3 scripts/new_problem.py

# Create new problem from LeetCode URL
python3 scripts/leetcode_setup.py

# Generate progress statistics
python3 scripts/generate_stats.py
```

## Architecture Overview

### Problem Organization System
- **Template-based**: All problems use standardized templates (`templates/problem_template.py`, `templates/test_template.py`)
- **Category-based**: Problems organized into 12 categories (arrays, strings, trees, graphs, etc.)
- **Numbered naming**: Problems follow `{number}_{sanitized_name}/` convention within categories
- **Mirrored structure**: Tests mirror the problems directory structure (`problems/category/001_name/` → `tests/category/001_name/`)

### Code Generation Workflow
1. `scripts/new_problem.py` prompts for problem details
2. Generates unique 3-digit number within category using `get_next_problem_number()`
3. Creates directory structure in both `problems/` and `tests/`
4. Populates files from templates with string substitution
5. Each problem gets: `solution.py`, `test_solution.py`, `README.md`

### Template System
- **problem_template.py**: Standardized Solution class with `solve()` method, time/space complexity placeholders, typing imports
- **test_template.py**: unittest.TestCase with common test patterns (examples, edge cases, performance tests)
- Templates use `{variable}` placeholders for dynamic content injection

### Progress Tracking
- `scripts/generate_stats.py` analyzes solved vs unsolved problems by parsing:
  - Directory structure for problem enumeration
  - `solution.py` files to detect implementation (checks if `solve()` method contains more than just `pass`)
  - README.md files for difficulty extraction
- Generates completion rates by category and difficulty

### Key Conventions
- Solution files must implement `solve()` method in `Solution` class
- Test files follow unittest framework with `TestSolution` class
- Problem directories named as `{3-digit-number}_{snake_case_name}`
- Each problem category is a separate directory under `problems/`
- Difficulty levels: Easy/Medium/Hard extracted from README metadata