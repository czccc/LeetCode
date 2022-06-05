#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = [0 for _ in range(len(triangle))]
        for i in range(len(triangle)):
            if i != 0:
                dp[i] = dp[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j - 1])
            dp[0] += triangle[i][0]
        ans = dp[0]
        for x in dp:
            ans = min(ans, x)
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
        cls._func = Solution().minimumTotal

    def test_1(self):
        args = [[
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]]
        ans = 11
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
