#!/usr/bin/env python3
"""
Script to generate statistics about solved LeetCode problems.
"""

import os
import json
from pathlib import Path
from collections import defaultdict, Counter
import re


def get_project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent


def get_problem_directories():
    """Get all problem directories organized by category."""
    project_root = get_project_root()
    problems_dir = project_root / "problems"
    
    problem_data = {}
    
    for category_dir in problems_dir.iterdir():
        if not category_dir.is_dir():
            continue
            
        category_name = category_dir.name
        problem_data[category_name] = []
        
        for problem_dir in category_dir.iterdir():
            if not problem_dir.is_dir():
                continue
                
            # Extract problem info from directory name and files
            problem_info = extract_problem_info(problem_dir)
            if problem_info:
                problem_data[category_name].append(problem_info)
    
    return problem_data


def extract_problem_info(problem_dir):
    """Extract problem information from a problem directory."""
    dir_name = problem_dir.name
    
    # Parse directory name (format: 001_problem_name)
    match = re.match(r'^(\d+)_(.+)$', dir_name)
    if not match:
        return None
    
    problem_number = match.group(1)
    problem_name = match.group(2).replace('_', ' ').title()
    
    # Check if solution exists
    solution_file = problem_dir / "solution.py"
    readme_file = problem_dir / "README.md"
    test_file = problem_dir.parent.parent.parent / "tests" / problem_dir.parent.name / problem_dir.name / "test_solution.py"
    
    # Extract difficulty from README if available
    difficulty = "Unknown"
    if readme_file.exists():
        try:
            with open(readme_file, 'r', encoding='utf-8') as f:
                content = f.read()
                difficulty_match = re.search(r'\*\*Difficulty:\*\*\s*(\w+)', content)
                if difficulty_match:
                    difficulty = difficulty_match.group(1)
        except Exception:
            pass
    
    # Check if solution is implemented (not just template)
    is_solved = False
    if solution_file.exists():
        try:
            with open(solution_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Check if the main method has been implemented (not just "pass")
                if 'def solve(' in content and not re.search(r'def solve\([^)]*\):\s*"""[^"]*"""\s*pass\s*$', content, re.MULTILINE):
                    is_solved = True
        except Exception:
            pass
    
    return {
        'number': problem_number,
        'name': problem_name,
        'difficulty': difficulty,
        'is_solved': is_solved,
        'has_tests': test_file.exists(),
        'directory': str(problem_dir)
    }


def generate_stats(problem_data):
    """Generate comprehensive statistics."""
    stats = {
        'total_problems': 0,
        'solved_problems': 0,
        'unsolved_problems': 0,
        'by_category': {},
        'by_difficulty': defaultdict(int),
        'solved_by_difficulty': defaultdict(int),
        'completion_rate': 0.0,
        'categories_summary': {}
    }
    
    for category, problems in problem_data.items():
        category_stats = {
            'total': len(problems),
            'solved': sum(1 for p in problems if p['is_solved']),
            'unsolved': sum(1 for p in problems if not p['is_solved']),
            'with_tests': sum(1 for p in problems if p['has_tests']),
            'completion_rate': 0.0,
            'problems': problems
        }
        
        if category_stats['total'] > 0:
            category_stats['completion_rate'] = (category_stats['solved'] / category_stats['total']) * 100
        
        stats['by_category'][category] = category_stats
        stats['categories_summary'][category] = {
            'total': category_stats['total'],
            'solved': category_stats['solved'],
            'completion_rate': category_stats['completion_rate']
        }
        
        # Update overall stats
        stats['total_problems'] += category_stats['total']
        stats['solved_problems'] += category_stats['solved']
        
        # Update difficulty stats
        for problem in problems:
            difficulty = problem['difficulty']
            stats['by_difficulty'][difficulty] += 1
            if problem['is_solved']:
                stats['solved_by_difficulty'][difficulty] += 1
    
    stats['unsolved_problems'] = stats['total_problems'] - stats['solved_problems']
    
    if stats['total_problems'] > 0:
        stats['completion_rate'] = (stats['solved_problems'] / stats['total_problems']) * 100
    
    return stats


def print_stats(stats):
    """Print formatted statistics."""
    print("📊 LeetCode Problem Tracker Statistics")
    print("=" * 50)
    
    # Overall stats
    print(f"\n🎯 Overall Progress:")
    print(f"   Total Problems: {stats['total_problems']}")
    print(f"   Solved: {stats['solved_problems']}")
    print(f"   Unsolved: {stats['unsolved_problems']}")
    print(f"   Completion Rate: {stats['completion_rate']:.1f}%")
    
    # Progress bar
    if stats['total_problems'] > 0:
        progress = int((stats['solved_problems'] / stats['total_problems']) * 20)
        bar = "█" * progress + "░" * (20 - progress)
        print(f"   Progress: [{bar}] {stats['completion_rate']:.1f}%")
    
    # Difficulty breakdown
    print(f"\n🎲 By Difficulty:")
    for difficulty in ['Easy', 'Medium', 'Hard', 'Unknown']:
        total = stats['by_difficulty'].get(difficulty, 0)
        solved = stats['solved_by_difficulty'].get(difficulty, 0)
        if total > 0:
            rate = (solved / total) * 100
            print(f"   {difficulty:8}: {solved:3}/{total:3} ({rate:5.1f}%)")
    
    # Category breakdown
    print(f"\n📁 By Category:")
    sorted_categories = sorted(stats['categories_summary'].items(), 
                             key=lambda x: x[1]['completion_rate'], reverse=True)
    
    for category, cat_stats in sorted_categories:
        if cat_stats['total'] > 0:
            print(f"   {category.replace('_', ' ').title():20}: "
                  f"{cat_stats['solved']:3}/{cat_stats['total']:3} "
                  f"({cat_stats['completion_rate']:5.1f}%)")
    
    # Recent activity (unsolved problems)
    print(f"\n📝 Unsolved Problems:")
    unsolved_count = 0
    for category, category_data in stats['by_category'].items():
        for problem in category_data['problems']:
            if not problem['is_solved']:
                if unsolved_count < 10:  # Show only first 10
                    print(f"   {problem['number']}. {problem['name']} "
                          f"({category.replace('_', ' ').title()}) - {problem['difficulty']}")
                unsolved_count += 1
    
    if unsolved_count > 10:
        print(f"   ... and {unsolved_count - 10} more")
    
    if unsolved_count == 0:
        print("   🎉 All problems solved! Great job!")


def save_stats_json(stats, output_file=None):
    """Save statistics to JSON file."""
    if output_file is None:
        output_file = get_project_root() / "stats.json"
    
    # Prepare data for JSON serialization
    json_stats = {
        'total_problems': stats['total_problems'],
        'solved_problems': stats['solved_problems'],
        'unsolved_problems': stats['unsolved_problems'],
        'completion_rate': stats['completion_rate'],
        'by_difficulty': dict(stats['by_difficulty']),
        'solved_by_difficulty': dict(stats['solved_by_difficulty']),
        'categories_summary': stats['categories_summary']
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_stats, f, indent=2)
    
    print(f"\n💾 Statistics saved to: {output_file}")


def main():
    """Main function to generate and display statistics."""
    try:
        print("🔍 Analyzing LeetCode problems...")
        
        # Get problem data
        problem_data = get_problem_directories()
        
        # Generate statistics
        stats = generate_stats(problem_data)
        
        # Print statistics
        print_stats(stats)
        
        # Save to JSON
        save_stats_json(stats)
        
        print(f"\n✨ Analysis complete!")
        
    except Exception as e:
        print(f"❌ Error generating statistics: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())