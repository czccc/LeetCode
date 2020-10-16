#
# @lc app=leetcode.cn id=52 lang=python
#
# [52] N皇后 II
#

# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def backtrack(i, ans):
            if i == n:
                return ans + 1
            for j in range(n):
                if row[i] and col[j] and left[i + j] and right[i - j]:
                    row[i] = 0
                    col[j] = 0
                    left[i + j] = 0
                    right[i - j] = 0
                    board[i][j] = "Q"

                    ans = backtrack(i + 1, ans)

                    row[i] = 1
                    col[j] = 1
                    left[i + j] = 1
                    right[i - j] = 1
                    board[i][j] = "."
            return ans

        row = [1 for i in range(n)]
        col = [1 for i in range(n)]
        left = [1 for i in range(n * 2 - 1)]
        right = [1 for i in range(n * 2 - 1)]
        ans = 0
        board = [["." for _ in range(n)] for i in range(n)]
        ans = backtrack(0, ans)
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
        cls._func = Solution().totalNQueens

    def test_1(self):
        args = [4]
        ans = 2
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [8]
        ans = 92
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
