#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        ans = []
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(matrix)
        n = len(matrix[0])
        cur_dir = 0
        cur_pos = [0, -1]
        while m and n:
            x, y = direction[cur_dir]
            cur_all = m if cur_dir % 2 else n
            for i in range(cur_all):
                cur_pos[0] += x
                cur_pos[1] += y
                ans.append(matrix[cur_pos[0]][cur_pos[1]])
            if cur_dir % 2:
                n -= 1
            else:
                m -= 1
            cur_dir = (cur_dir + 1) % 4
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
        cls._func = Solution().spiralOrder

    def test_1(self):
        args = [[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]]
        ans = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)

    def test_2(self):
        args = [[
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]]
        ans = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
