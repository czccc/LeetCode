#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def backtrack(i):
            if i == n:
                ans.append([])
                for i in range(n):
                    ans[-1].append("".join(board[i]))
                return
            for j in range(n):
                if row[i] and col[j] and left[i + j] and right[i - j]:
                    row[i] = 0
                    col[j] = 0
                    left[i + j] = 0
                    right[i - j] = 0
                    board[i][j] = "Q"

                    backtrack(i + 1)

                    row[i] = 1
                    col[j] = 1
                    left[i + j] = 1
                    right[i - j] = 1
                    board[i][j] = "."

        row = [1 for i in range(n)]
        col = [1 for i in range(n)]
        left = [1 for i in range(n * 2 - 1)]
        right = [1 for i in range(n * 2 - 1)]
        ans = []
        board = [["." for _ in range(n)] for i in range(n)]
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
        cls._func = Solution().solveNQueens

    def test_1(self):
        args = [4]
        ans = [
            [".Q..",
             "...Q",
             "Q...",
             "..Q."],

            ["..Q.",
             "Q...",
             "...Q",
             ".Q.."]
        ]
        cur_ans = self._func(*args)
        # self.assertEqual(set(cur_ans), set(ans))
        self.assertSequenceEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
