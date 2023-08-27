#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.cn/problems/n-queens/description/
#
# algorithms
# Hard (74.05%)
# Likes:    1872
# Dislikes: 0
# Total Accepted:    328.1K
# Total Submissions: 443.1K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You
# may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [["Q"]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 9
#
#
#


from leetcode.before import *


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        ret = []

        def isvalid(i, j):
            for x in range(len(board)):
                if x < i and board[x][j] == "Q":
                    return False
                if x < j and board[i][x] == "Q":
                    return False
                if i - x >= 0 and j - x >= 0 and board[i - x][j - x] == "Q":
                    return False
                if i - x >= 0 and j + x < len(board) and board[i - x][j + x] == "Q":
                    return False
            return True

        def queens(i, board):
            if i == len(board):
                tmp = []
                for x in board:
                    tmp.append("".join(x))
                ret.append(tmp)
                return
            for j in range(n):
                if not isvalid(i, j):
                    continue
                board[i][j] = "Q"
                queens(i + 1, board)
                board[i][j] = "."

        queens(0, board)
        return ret


# @lc code=end

from leetcode.after import *


class SolutionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._func = Solution().solveNQueens

    def test_1(self):
        args = [4]
        ans = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        ret = self._func(*args)
        self.assertEqual(ret, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
