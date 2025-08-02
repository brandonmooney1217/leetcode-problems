"""
Unit tests for LeetCode Problem: 128. Longest Consecutive sequence
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
                 "problems", "arrays", "002_longest_consecutive_sequence", "solution.py")
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
        """Test example case 1: nums = [100,4,200,1,3,2], expected = 4."""
        # Arrange
        nums = [100, 4, 200, 1, 3, 2]
        expected = 4
        
        # Act
        result = self.solution.solve(nums)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        """Test example case 2: nums = [0,3,7,2,5,8,4,6,0,1], expected = 9."""
        # Arrange
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        expected = 9
        
        # Act
        result = self.solution.solve(nums)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_example_3(self):
        """Test example case 3: nums = [1,0,1,2], expected = 3."""
        # Arrange
        nums = [1, 0, 1, 2]
        expected = 3
        
        # Act
        result = self.solution.solve(nums)
        
        # Assert
        self.assertEqual(result, expected)
    
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
    unittest.main(verbosity=2)