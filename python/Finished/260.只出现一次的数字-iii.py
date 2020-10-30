#
# @lc app=leetcode.cn id=260 lang=python
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all = 0
        for x in nums:
            all ^= x
        # bitmask = all & (-all)
        bitmask = 1
        while not all & bitmask:
            bitmask <<= 1
        one = two = 0
        # two = one ^ all
        for x in nums:
            if bitmask & x:
                one ^= x
            else:
                two ^= x
        return one, two
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
        args = [[1, 2, 1, 3, 2, 5]]
        ans = [3, 5]
        cur_ans = self._func(*args)
        self.assertSequenceEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
