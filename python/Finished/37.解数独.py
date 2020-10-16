#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_valid(i, j, cur):
            if cur in row[i] and cur in col[j] and cur in squ[i // 3 * 3 + j // 3]:
                return True
            else:
                return False

        def backtrack(i, j):
            if j == 9:
                return backtrack(i + 1, 0)
            if i == 9:
                return True
            if board[i][j] != ".":
                return backtrack(i, j + 1)
            for cur in [str(i + 1) for i in range(9)]:
                if not is_valid(i, j, cur):
                    continue

                row[i].remove(cur)
                col[j].remove(cur)
                squ[i // 3 * 3 + j // 3].remove(cur)
                board[i][j] = cur

                if backtrack(i, j + 1):
                    return True

                board[i][j] = "."
                row[i].append(cur)
                col[j].append(cur)
                squ[i // 3 * 3 + j // 3].append(cur)
            return False

        row = [[str(i + 1) for i in range(9)] for j in range(9)]
        col = [[str(i + 1) for i in range(9)] for j in range(9)]
        squ = [[str(i + 1) for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != ".":
                    row[i].remove(cur)
                    col[j].remove(cur)
                    squ[i // 3 * 3 + j // 3].remove(cur)
        backtrack(0, 0)
        return

# @lc code=end


# TEST ONLY
import unittest
import sys
sys.path.append("..")
from Base.PyVar import *

class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().solveSudoku

    def test_1(self):
        args = [[["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]]
        ans = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
               ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
               ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
               ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
               ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
               ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
               ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
               ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
               ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
        cur_ans = self._func(*args)
        self.assertEqual(args[0], ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
