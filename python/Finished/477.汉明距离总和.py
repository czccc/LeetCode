#
# @lc app=leetcode.cn id=477 lang=python
#
# [477] 汉明距离总和
#

# @lc code=start
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cnt = [0] * 32
        for x in nums:
            for i in range(32):
                if x & (1 << i):
                    cnt[i] += 1
        for c in cnt:
            ans += c * (len(nums) - c)
        return ans
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().totalHammingDistance

    def test_1(self):
        args = [[4, 14, 2]]
        ans = 6
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
