#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        i = 0
        j = len(height) - 1
        while i < j:
            cur = (j - i) * min(height[i], height[j])
            ans = max(ans, cur)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
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
        cls._func = Solution().maxArea

    def test_1(self):
        args = [[1, 8, 6, 2, 5, 4, 8, 3, 7]]
        ans = 49
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
