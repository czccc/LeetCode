#
# @lc app=leetcode.cn id=405 lang=python
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        hexchar = "0123456789abcdef"
        ans = ["0"] * 8
        mask = 15
        for i in range(8):
            res = (num >> (4 * i)) & mask
            ans[7 - i] = hexchar[res]
        for i in range(7):
            if ans[i] != "0":
                return "".join(ans[i:])
        return ans[7]

# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().toHex

    def test_1(self):
        args = [-1]
        ans = "ffffffff"
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [26]
        ans = "1a"
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
