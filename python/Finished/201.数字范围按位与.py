#
# @lc app=leetcode.cn id=201 lang=python
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            shift += 1
        return n << shift
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().rangeBitwiseAnd

    def test_1(self):
        args = [5, 7]
        ans = 4
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
