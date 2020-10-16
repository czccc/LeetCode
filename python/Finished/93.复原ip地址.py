#
# @lc app=leetcode.cn id=93 lang=python
#
# [93] 复原IP地址
#

# @lc code=start
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(i, j):
            j = min(len(s), j)
            if i >= j:
                return False
            num = int(s[i:j])
            if j - i == 2 and num < 10:
                return False
            elif j - i == 3 and num < 100:
                return False
            elif num > 255:
                return False
            return True

        def backtrack(i):
            if len(build) == 4:
                if i == len(s):
                    ans.append(".".join(build))
                return
            for k in range(3):
                if is_valid(i, i + k + 1):
                    build.append(s[i:i + k + 1])
                    backtrack(i + k + 1)
                    build.pop()
        ans = []
        build = []
        backtrack(0)
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
        cls._func = Solution().restoreIpAddresses

    def test_1(self):
        args = ["25525511135"]
        ans = ["255.255.11.135", "255.255.111.35"]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = ["0000"]
        ans = ["0.0.0.0"]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_3(self):
        args = ["1111"]
        ans = ["1.1.1.1"]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_4(self):
        args = ["010010"]
        ans = ["0.10.0.10", "0.100.1.0"]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
