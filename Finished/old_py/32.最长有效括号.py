#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ans = 0
        index = [-1 for _ in range(len(s))]
        dp = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                dp.append(i)
            else:
                dp.pop()
                if not dp:
                    dp.append(i)
                else:
                    ans = max(ans, i - dp[-1])
        return ans


# @lc code=end

# TEST ONLY
import unittest

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().longestValidParentheses

    def test_normal(self):
        args = ["(()"]
        ans = 2
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_1(self):
        args = [")()())"]
        ans = 4
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = ["(()()(()((()())()))"]
        ans = 18
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
