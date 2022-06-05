#
# @lc app=leetcode.cn id=389 lang=python
#
# [389] 找不同
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = ord(t[-1])
        for i in range(len(s)):
            ans ^= ord(s[i])
            ans ^= ord(t[i])
        return chr(ans)
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().findTheDifference

    def test_1(self):
        args = ["abcd", "abcde"]
        ans = "e"
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
