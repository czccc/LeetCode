#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            i = start
            j = end - 1
            while i < j:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                i += 1
                j -= 1
        k %= len(nums)
        reverse(0, len(nums))
        reverse(0, k)
        reverse(k, len(nums))
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().rotate

    def test_1(self):
        args = [[1, 2, 3, 4, 5, 6, 7], 3]
        ans = [5, 6, 7, 1, 2, 3, 4]
        cur_ans = self._func(*args)
        self.assertEqual(args[0], ans)

    def test_2(self):
        args = [[-1, -100, 3, 99], 2]
        ans = [3, 99, -1, -100]
        cur_ans = self._func(*args)
        self.assertEqual(args[0], ans)

    def test_3(self):
        args = [[-1], 2]
        ans = [-1]
        cur_ans = self._func(*args)
        self.assertEqual(args[0], ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
