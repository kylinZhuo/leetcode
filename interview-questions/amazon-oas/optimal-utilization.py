"""
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. 
Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. 
Return a list of ids of selected elements. If no pair is possible, return an empty list.

Example 1:

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.

Example 2:

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].


"""

import unittest

class Solution(object):

    def function(self, arr1, arr2, target):

        arr1 = sorted(arr1, key = lambda x : x[1])
        arr2 = sorted(arr2, key = lambda x : x[1])
        
        left, right = 0, len(arr2) - 1
        diff = float('inf')
        res = []

        while left < len(arr1) and right >= 0:
            id1, val1 = arr1[left]
            id2, val2 = arr2[right]
            new_diff = target - val1 - val2 
            if new_diff == diff:
                res.append([id1, id2])
            elif 0 <= new_diff < diff:
                diff = new_diff
                res.clear()
                res.append([id1, id2])
            if new_diff > 0:
                left += 1
            else:
                right -= 1
        
        return res 

class Test(unittest.TestCase):

    s = Solution()
    
    def test1(self):
        a = [[1, 2], [2, 4], [3, 6]]
        b = [[1, 2]]
        target = 7
        self.assertEqual(self.s.function(a, b, target), [[2, 1]])

    def test2(self):
        a = [[1, 3], [2, 5], [3, 7], [4, 10]]
        b = [[1, 2], [2, 3], [3, 4], [4, 5]]
        target = 10
        self.assertEqual(self.s.function(a, b, target), [[2, 4], [3, 2]])

    def test3(self):
        a = [[1, 8], [2, 7], [3, 14]]
        b = [[1, 5], [2, 10], [3, 14]]
        target = 20
        self.assertEqual(self.s.function(a, b, target), [[3, 1]])

    def test4(self):
        a = [[1, 8], [2, 15], [3, 9]]
        b = [[1, 8], [2, 11], [3, 12]]
        target = 20

        self.assertEqual(self.s.function(a, b, target), [[1, 3], [3, 2]])

if __name__ == '__main__':
    unittest.main()
    