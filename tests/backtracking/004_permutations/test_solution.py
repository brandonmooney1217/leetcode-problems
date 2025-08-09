"""
Unit tests for LeetCode Problem: 004. Permutations
"""

import unittest
import sys
import os

# Add the parent directory to sys.path to import the solution
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

# Import using importlib to handle directory names starting with numbers
import importlib.util
spec = importlib.util.spec_from_file_location(
    "solution", 
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 
                 "problems", "backtracking", "004_permutations", "solution.py")
)
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution


class TestSolution(unittest.TestCase):
    """Test cases for the solution."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test example case 1: nums = [1,2,3]."""
        # Arrange
        nums = [1, 2, 3]
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        
        # Act
        result = self.solution.solve(nums)
        
        # Assert
        self.assertEqual(len(result), len(expected))
        for perm in result:
            self.assertIn(perm, expected)
        for perm in expected:
            self.assertIn(perm, result)
    
    def test_example_2(self):
        """Test example case 2: nums = [0,1]."""
        # Arrange
        nums = [0, 1]
        expected = [[0,1],[1,0]]
        
        # Act
        result = self.solution.solve(nums)
        
        # Assert
        self.assertEqual(len(result), len(expected))
        for perm in result:
            self.assertIn(perm, expected)
        for perm in expected:
            self.assertIn(perm, result)
    
    def test_example_3(self):
        """Test example case 3: nums = [1]."""
        # Arrange
        nums = [1]
        expected = [[1]]
        
        # Act
        result = self.solution.solve(nums)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_edge_case_empty(self):
        """Test edge case with empty input."""
        # Arrange
        nums = []
        expected = [[]]
        
        # Act
        result = self.solution.solve(nums)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_edge_case_two_elements(self):
        """Test edge case with two different elements."""
        # Arrange
        nums = [1, 2]
        expected = [[1,2],[2,1]]
        
        # Act
        result = self.solution.solve(nums)
        
        # Assert
        self.assertEqual(len(result), len(expected))
        for perm in result:
            self.assertIn(perm, expected)
        for perm in expected:
            self.assertIn(perm, result)


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
    unittest.main(verbosity=2)