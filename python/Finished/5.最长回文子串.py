#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ans = s[0]
        for i in range(len(s)):
            dp[i][i] = True
            if i + 1 < len(s) and s[i] == s[i + 1]:
                ans = s[i:i + 2]
                dp[i][i + 1] = True
        for delta in range(2, len(s)):
            for i in range(len(s) - delta):
                if dp[i + 1][i + delta - 1] and s[i] == s[i + delta]:
                    ans = s[i:i + delta + 1]
                    dp[i][i + delta] = True
        return ans
# @lc code=end


# TEST ONLY
import unittest

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().longestPalindrome

    def test_none(self):
        args = [""]
        ans = [""]
        cur_ans = self._func(*args)
        self.assertTrue(cur_ans in ans)

    def test_normal(self):
        args = ["babad"]
        ans = ["aba", "bab"]
        cur_ans = self._func(*args)
        self.assertTrue(cur_ans in ans)

    def test_one(self):
        args = ["cbd"]
        ans = ["c", "b", "d"]
        cur_ans = self._func(*args)
        self.assertTrue(cur_ans in ans)

    def test_double(self):
        args = ["cbbd"]
        ans = ["bb"]
        cur_ans = self._func(*args)
        self.assertTrue(cur_ans in ans)

    def test_all(self):
        args = ["abcba"]
        ans = ["abcba"]
        cur_ans = self._func(*args)
        self.assertTrue(cur_ans in ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
