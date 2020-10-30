#
# @lc app=leetcode.cn id=693 lang=python
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = (n ^ (n >> 1)) + 1
        return t & (t - 1) == 0
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().hasAlternatingBits

    def test_1(self):
        args = [5]
        ans = True
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [7]
        ans = False
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
