#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            left = s[i]
            right = s[j]
            if not left.isalnum():
                i += 1
            elif not right.isalnum():
                j -= 1
            elif left.upper() == right.upper():
                i += 1
                j -= 1
            else:
                return False
        return True
# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().isPalindrome

    def test_1(self):
        args = ["A man, a plan, a canal: Panama"]
        ans = True
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = ["race a car"]
        ans = False
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
