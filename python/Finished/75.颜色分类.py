#
# @lc app=leetcode.cn id=75 lang=python
#
# [75] 颜色分类
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, right = -1, len(nums)
        p = 0
        while p < right:
            if nums[p] == 2:
                right -= 1
                nums[p] = nums[right]
                nums[right] = 2
            elif nums[p] == 1:
                p += 1
            else:
                left += 1
                nums[p] = 1
                nums[left] = 0
                p += 1
        return
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().sortColors

    def test_1(self):
        args = [[2, 0, 2, 1, 1, 0]]
        ans = [0, 0, 1, 1, 2, 2]
        cur_ans = self._func(*args)
        self.assertEqual(args[0], ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
