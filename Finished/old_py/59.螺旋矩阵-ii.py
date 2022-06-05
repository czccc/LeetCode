#
# @lc app=leetcode.cn id=59 lang=python
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = n
        ans = [[0 for _ in range(n)] for _ in range(n)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur_dir = 0
        cur_pos = [0, -1]
        cur_num = 0
        while m and n:
            x, y = direction[cur_dir]
            cur_all = m if cur_dir % 2 else n
            for i in range(cur_all):
                cur_pos[0] += x
                cur_pos[1] += y
                cur_num += 1
                ans[cur_pos[0]][cur_pos[1]] = cur_num
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
        cls._func = Solution().generateMatrix

    def test_1(self):
        args = [3]
        ans = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        cur_ans = self._func(*args)
        self.assertEqual(cur_ans, ans)


if __name__ == "__main__":
    unittest.main(verbosity=2)
