#
# @lc app=leetcode.cn id=162 lang=python
#
# [162] 寻找峰值
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        e = len(nums) - 1
        while (s < e):
            m = (s + e) // 2
            if nums[m] > nums[m + 1]:
                e = m
            else:
                s = m + 1
        return s
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().findPeakElement

    def test_1(self):
        args = [[1, 2, 3, 1]]
        ans = 2
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
