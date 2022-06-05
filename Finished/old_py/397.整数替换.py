#
# @lc app=leetcode.cn id=397 lang=python
#
# [397] 整数替换
#

# @lc code=start
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = 0
        while n >= 4:
            step += 1
            if n & 1 == 0:
                n //= 2
            elif n & 3 == 3:
                n += 1
            else:
                n -= 1
        return step + n - 1
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().integerReplacement

    def test_1(self):
        args = [8]
        ans = 3
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
