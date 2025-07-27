import unittest

from findMaxSum import findMaxSum

class TestFindMaxSum(unittest.TestCase):

    def testEmpty(self):
        """Test returns 0 on empty array."""
        strings = []
        stringsSum = findMaxSum(strings)
        self.assertEqual(stringsSum, 0)

    def testFullOFEmptys(self):
        """Test returns 0 on array filled with empty strings."""
        strings = ['', '', '']
        stringsSum = findMaxSum(strings)
        self.assertEqual(stringsSum, 0)

    def testNoNumerics(self):
        """Test returns 0 on array with strings containing no numbers."""
        strings = ['ab', 'cd', 'ef', 'gh']
        stringsSum = findMaxSum(strings)
        self.assertEqual(stringsSum, 0)

    def testSmallSum(self):
        """Test with valid data of normal size."""
        strings = ['a101', 'b2005', 'c302', 'd404']
        stringsSum = findMaxSum(strings)
        self.assertEqual(stringsSum, 8) # d404, 4 + 0 + 4 = 8
    
    def testMaxSize(self):
        """Test with the (self-imposed, arbitrary) max size limits."""
        strings = ['aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa']
        stringsSum = findMaxSum(strings)
        self.assertEqual(stringsSum, 0)