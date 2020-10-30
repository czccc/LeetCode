#
# @lc app=leetcode.cn id=190 lang=python
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n % 2)
            n >>= 1
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
        cls._func = Solution().reverseBits

    def test_1(self):
        args = [43261596]
        ans = 964176192
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [4294967293]
        ans = 3221225471
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
