#
# @lc app=leetcode.cn id=338 lang=python
#
# [338] 比特位计数
#

# @lc code=start
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0 for i in range(num + 1)]
        pre = 0
        mod = 1
        for i in range(1, num + 1):
            if i == mod:
                pre = mod
                mod <<= 1
            if i - pre < (mod - pre) // 2:
                ans[i] = ans[pre // 2 + i - pre]
            else:
                ans[i] = ans[pre // 2 + i - pre] + 1
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
        cls._func = Solution().countBits

    def test_1(self):
        args = [17]
        ans = [0,
               1,
               1, 2,
               1, 2, 2, 3,
               1, 2, 2, 3, 2, 3, 3, 4,
               1, 2]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [65]
        ans = [0,
               1,
               1, 2,
               1, 2, 2, 3,
               1, 2, 2, 3, 2, 3, 3, 4,
               1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
               1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
               1, 2]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
