#!/usr/bin/env python3
"""
Simple script to create a new LeetCode problem template.
Just creates empty files for you to fill in.
"""

import os
import re
from pathlib import Path


def get_project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent


def get_categories():
    """Get available problem categories."""
    problems_dir = get_project_root() / "problems"
    return [d.name for d in problems_dir.iterdir() if d.is_dir()]


def sanitize_filename(name):
    """Sanitize a string to be used as a filename."""
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'\s+', '_', name)
    return name.lower()


def get_next_problem_number(category_path):
    """Get the next problem number for a category."""
    if not category_path.exists():
        return "001"
    
    problem_dirs = [d for d in category_path.iterdir() if d.is_dir()]
    if not problem_dirs:
        return "001"
    
    numbers = []
    for d in problem_dirs:
        match = re.match(r'^(\d+)_', d.name)
        if match:
            numbers.append(int(match.group(1)))
    
    if numbers:
        return f"{max(numbers) + 1:03d}"
    else:
        return "001"


def create_problem_structure(category, problem_name):
    """Create the problem directory structure."""
    project_root = get_project_root()
    sanitized_name = sanitize_filename(problem_name)
    
    # Get next available number for this category
    category_path = project_root / "problems" / category
    next_number = get_next_problem_number(category_path)
    
    dir_name = f"{next_number}_{sanitized_name}"
    
    # Create problem directory
    problem_dir = project_root / "problems" / category / dir_name
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    # Create corresponding test directory
    test_dir = project_root / "tests" / category / dir_name
    test_dir.mkdir(parents=True, exist_ok=True)
    
    return problem_dir, test_dir, next_number


def create_solution_file(problem_dir, problem_name, category, local_number, leetcode_number=None):
    """Create the solution.py file with basic template."""
    leetcode_num = leetcode_number if leetcode_number else "?"
    leetcode_url = f"https://leetcode.com/problems/{problem_name.lower().replace(' ', '-')}/" if leetcode_number else "?"
    
    content = f'''"""
LeetCode Problem: {leetcode_num}. {problem_name}

Difficulty: ?
Category: {category}
URL: {leetcode_url}

Problem Description:
Add problem description here.

Constraints:
Add constraints here.

Examples:
Add examples here.
"""

from typing import List, Optional, Dict, Set


class Solution:
    def solve(self):
        """
        Main solution method - IMPLEMENT YOUR SOLUTION HERE.
        
        Time Complexity: O(?)
        Space Complexity: O(?)
        
        Approach:
        1. Add your approach here
        2. 
        3. 
        
        Args:
            Add function parameters here
        
        Returns:
            Add return type description here
        """
        # TODO: Implement your solution here
        pass


def main():
    """Test the solution with example cases."""
    solution = Solution()
    
    # TODO: Add test cases here
    # Test case 1
    # result = solution.solve()
    # print(f"Test 1 - Expected: ?, Got: {{result}}")
    
    # Test case 2
    # result = solution.solve()
    # print(f"Test 2 - Expected: ?, Got: {{result}}")


if __name__ == "__main__":
    main()'''
    
    solution_path = problem_dir / "solution.py"
    with open(solution_path, 'w', encoding='utf-8') as f:
        f.write(content)


def create_test_file(test_dir, problem_name, category, local_number, leetcode_number=None):
    """Create the test_solution.py file with basic template."""
    sanitized_name = sanitize_filename(problem_name)
    leetcode_num = leetcode_number if leetcode_number else "?"
    
    content = f'''"""
Unit tests for LeetCode Problem: {leetcode_num}. {problem_name}
"""

import unittest
import sys
import os

# Add the parent directory to sys.path to import the solution
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from problems.{category}.{local_number}_{sanitized_name}.solution import Solution


class TestSolution(unittest.TestCase):
    """Test cases for the solution."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test example case 1 - UPDATE WITH ACTUAL TEST."""
        # TODO: Replace with actual test case from LeetCode
        # Arrange
        input_data = None  # Replace with actual input
        expected = None    # Replace with expected output
        
        # Act
        # result = self.solution.solve(input_data)
        
        # Assert
        # self.assertEqual(result, expected)
        pass
    
    def test_example_2(self):
        """Test example case 2 - UPDATE WITH ACTUAL TEST."""
        # TODO: Replace with actual test case from LeetCode
        # Arrange
        input_data = None  # Replace with actual input
        expected = None    # Replace with expected output
        
        # Act
        # result = self.solution.solve(input_data)
        
        # Assert
        # self.assertEqual(result, expected)
        pass
    
    def test_edge_case_minimum(self):
        """Test edge case with minimum constraint values - UPDATE AS NEEDED."""
        # TODO: Add minimum constraint test
        pass
    
    def test_edge_case_maximum(self):
        """Test edge case with maximum constraint values - UPDATE AS NEEDED."""
        # TODO: Add maximum constraint test
        pass


class TestSolutionPerformance(unittest.TestCase):
    """Performance tests for the solution."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def test_large_input_performance(self):
        """Test solution performance with large input - UPDATE AS NEEDED."""
        # TODO: Create performance test based on problem constraints
        pass


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)'''
    
    test_path = test_dir / "test_solution.py"
    with open(test_path, 'w', encoding='utf-8') as f:
        f.write(content)


def create_readme_file(problem_dir, problem_name, leetcode_number=None):
    """Create the README.md file with basic template."""
    leetcode_num = leetcode_number if leetcode_number else "?"
    leetcode_url = f"https://leetcode.com/problems/{problem_name.lower().replace(' ', '-')}/" if leetcode_number else "?"
    
    content = f"""# {leetcode_num}. {problem_name}

**Difficulty:** ?  
**Category:** ?  
**URL:** [LeetCode]({leetcode_url})

## Problem Description

Add problem description here.

## Constraints

Add constraints here.

## Examples

Add examples here.

## Approach

Add your approach and explanation here after solving.

## Time and Space Complexity

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

## Notes

Add any additional notes, alternative approaches, or learnings here.
"""
    
    readme_path = problem_dir / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    """Main function to create a new problem."""
    print("🚀 New LeetCode Problem")
    print("=" * 25)
    
    # Get LeetCode problem number
    while True:
        problem_number = input("Enter LeetCode problem number: ").strip()
        if not problem_number:
            print("❌ Problem number cannot be empty!")
            continue
        if not problem_number.isdigit():
            print("❌ Problem number must be a number!")
            continue
        break
    
    # Get problem name
    problem_name = input("Enter problem name: ").strip()
    if not problem_name:
        print("❌ Problem name cannot be empty!")
        return 1
    
    # Get available categories
    categories = get_categories()
    print(f"Available categories: {', '.join(categories)}")
    
    # Get category from user
    while True:
        category = input("Enter problem category: ").strip().lower()
        if category in categories:
            break
        print(f"Invalid category. Please choose from: {', '.join(categories)}")
    
    # Create directory structure
    problem_dir, test_dir, local_number = create_problem_structure(category, problem_name)
    
    # Create files with LeetCode problem number
    create_solution_file(problem_dir, problem_name, category, local_number, problem_number)
    create_test_file(test_dir, problem_name, category, local_number, problem_number)
    create_readme_file(problem_dir, problem_name, problem_number)
    
    print(f"✅ Successfully created problem template:")
    print(f"   📁 Problem: {problem_dir}")
    print(f"   📁 Tests: {test_dir}")
    print(f"   📝 Files created:")
    print(f"      - solution.py (empty template)")
    print(f"      - test_solution.py (placeholder tests)")
    print(f"      - README.md (basic template)")
    print(f"\n🎯 Ready for you to:")
    print(f"   1. Fill in problem details in README.md")
    print(f"   2. Implement solution in solution.py")
    print(f"   3. Add test cases in test_solution.py")
    print(f"\n📝 Edit: {problem_dir / 'solution.py'}")
    
    return 0


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        exit(1)