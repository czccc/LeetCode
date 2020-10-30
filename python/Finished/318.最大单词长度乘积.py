#
# @lc app=leetcode.cn id=318 lang=python
#
# [318] 最大单词长度乘积
#

# @lc code=start
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def char2int(c):
            return ord(c) - ord("a")

        mask = dict()
        for x in words:
            cur = 0
            for c in x:
                cur |= 1 << char2int(c)
            mask[cur] = max(len(x), mask.get(cur, 0))
        ans = 0
        for k1, v1 in mask.items():
            for k2, v2 in mask.items():
                if not k1 & k2:
                    ans = max(ans, v1 * v2)
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
        cls._func = Solution().maxProduct

    def test_1(self):
        args = [["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]]
        ans = 16
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [["a", "ab", "abc", "d", "cd", "bcd", "abcd"]]
        ans = 4
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_3(self):
        args = [["a", "aa", "aaa", "aaaa"]]
        ans = 0
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
