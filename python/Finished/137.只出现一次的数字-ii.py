#
# @lc app=leetcode.cn id=137 lang=python
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen_once = seen_twice = 0
        for x in nums:
            seen_once = ~seen_twice & (seen_once ^ x)
            seen_twice = ~seen_once & (seen_twice ^ x)
        return seen_once
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().singleNumber

    def test_1(self):
        args = [[2, 2, 2, 3]]
        ans = 3
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [[0, 1, 0, 1, 0, 1, 99]]
        ans = 99
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
