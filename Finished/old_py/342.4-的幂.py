#
# @lc app=leetcode.cn id=342 lang=python
#
# [342] 4的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and \
            (num & (num - 1)) == 0 and \
            (num & 0x55555555) > 0

# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().isPowerOfFour

    def test_1(self):
        args = [1024]
        ans = True
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
