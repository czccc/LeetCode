#
# @lc app=leetcode.cn id=80 lang=python
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        i = 0
        j = 1
        count = 1
        while j < len(nums):
            if nums[j - 1] == nums[j]:
                count += 1
            else:
                count = 1
            if count <= 2:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().removeDuplicates

    def test_1(self):
        args = [[1, 1, 1, 2, 2, 3]]
        ans = [1, 1, 2, 2, 3]
        cur_ans = self._func(*args)
        self.assertEqual(args[0][:cur_ans], ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
