#!/usr/bin/env python3
"""
Script to generate a new LeetCode problem structure from templates.
"""

import os
import sys
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
    # Remove or replace invalid characters
    name = re.sub(r'[^\w\s-]', '', name)
    # Replace spaces with underscores
    name = re.sub(r'\s+', '_', name)
    # Convert to lowercase
    return name.lower()


def get_next_problem_number(category_path):
    """Get the next problem number for a category."""
    if not category_path.exists():
        return "001"
    
    problem_dirs = [d for d in category_path.iterdir() if d.is_dir()]
    if not problem_dirs:
        return "001"
    
    # Extract numbers from existing directories
    numbers = []
    for d in problem_dirs:
        match = re.match(r'^(\d+)_', d.name)
        if match:
            numbers.append(int(match.group(1)))
    
    if numbers:
        return f"{max(numbers) + 1:03d}"
    else:
        return "001"


def create_problem_directory(category, problem_number, problem_name):
    """Create the problem directory structure."""
    project_root = get_project_root()
    sanitized_name = sanitize_filename(problem_name)
    dir_name = f"{problem_number}_{sanitized_name}"
    
    # Create problem directory
    problem_dir = project_root / "problems" / category / dir_name
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    # Create corresponding test directory
    test_dir = project_root / "tests" / category / dir_name
    test_dir.mkdir(parents=True, exist_ok=True)
    
    return problem_dir, test_dir


def load_template(template_name):
    """Load a template file."""
    project_root = get_project_root()
    template_path = project_root / "templates" / template_name
    
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def create_problem_files(problem_dir, test_dir, problem_data):
    """Create the problem files from templates."""
    # Create solution.py
    solution_template = load_template("problem_template.py")
    solution_content = solution_template.format(**problem_data)
    
    solution_path = problem_dir / "solution.py"
    with open(solution_path, 'w', encoding='utf-8') as f:
        f.write(solution_content)
    
    # Create test_solution.py
    test_template = load_template("test_template.py")
    test_content = test_template.format(**problem_data)
    
    test_path = test_dir / "test_solution.py"
    with open(test_path, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    # Create README.md for the problem
    readme_content = f"""# {problem_data['problem_number']}. {problem_data['problem_name']}

**Difficulty:** {problem_data['difficulty']}  
**Category:** {problem_data['category']}  
**URL:** [LeetCode](https://leetcode.com/problems/{problem_data['problem_url']}/)

## Problem Description

{problem_data.get('problem_description', 'Add problem description here.')}

## Constraints

{problem_data.get('constraints', 'Add constraints here.')}

## Example

{problem_data.get('example', 'Add example here.')}

## Approach

Add your approach and explanation here.

## Time and Space Complexity

- **Time Complexity:** O()
- **Space Complexity:** O()

## Notes

Add any additional notes, alternative approaches, or learnings here.
"""
    
    readme_path = problem_dir / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)


def main():
    """Main function to create a new problem."""
    print("🚀 LeetCode Problem Generator")
    print("=" * 30)
    
    # Get available categories
    categories = get_categories()
    print(f"Available categories: {', '.join(categories)}")
    
    # Get user input
    while True:
        category = input("Enter problem category: ").strip().lower()
        if category in categories:
            break
        print(f"Invalid category. Please choose from: {', '.join(categories)}")
    
    problem_name = input("Enter problem name: ").strip()
    if not problem_name:
        print("Problem name cannot be empty!")
        return
    
    # Get optional inputs
    difficulty = input("Enter difficulty (Easy/Medium/Hard) [Medium]: ").strip() or "Medium"
    problem_description = input("Enter problem description (optional): ").strip() or "Add problem description here."
    constraints = input("Enter constraints (optional): ").strip() or "Add constraints here."
    example = input("Enter example (optional): ").strip() or "Add example here."
    
    # Generate problem number
    category_path = get_project_root() / "problems" / category
    problem_number = get_next_problem_number(category_path)
    
    # Create problem URL
    problem_url = sanitize_filename(problem_name).replace('_', '-')
    
    # Prepare problem data
    problem_data = {
        'problem_number': problem_number,
        'problem_name': problem_name,
        'difficulty': difficulty,
        'category': category,
        'problem_url': problem_url,
        'problem_description': problem_description,
        'constraints': constraints,
        'example': example
    }
    
    # Create directories
    problem_dir, test_dir = create_problem_directory(category, problem_number, problem_name)
    
    # Create files
    create_problem_files(problem_dir, test_dir, problem_data)
    
    print(f"\n✅ Successfully created problem structure:")
    print(f"   📁 Problem: {problem_dir}")
    print(f"   📁 Tests: {test_dir}")
    print(f"   📝 Files created:")
    print(f"      - solution.py")
    print(f"      - test_solution.py")
    print(f"      - README.md")
    print(f"\n🎯 You can now start coding your solution!")
    print(f"   Problem file: {problem_dir / 'solution.py'}")
    print(f"   Test file: {test_dir / 'test_solution.py'}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)